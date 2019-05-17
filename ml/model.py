print("Model imported!!")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from tqdm import tqdm
import numpy as np
import pandas as pd
import spacy
import pickle
import re

vectorizer = pickle.load(open("./ml/vectorizer.pkl", "rb"))
sk_nblearn = pickle.load(open("./ml/sk_nblearn.pkl", "rb"))
# python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm', disable=["tagger", "parser", "ner", "textcat"])

# function to clean text data
def clean_desc(desc):
    clean_1 = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    clean_2 = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

    desc = [clean_1.sub("", line.lower()) for line in desc]
    desc = [clean_2.sub(" ", line) for line in desc]
    return desc


# tokenization using spaCy
def tokenization(x):
    desc_tokens = []
    for i in tqdm(x):
        i = nlp(i)
        temp = []
        for j in i:
            temp.append(j.text)
        desc_tokens.append(temp)
    
    return desc_tokens
  

# function to remove stopwords
def remove_stopwords(desc):
    s = []
    for r in tqdm(desc):
        s_2 = []
        for token in r:
            if nlp.vocab[token].is_stop == True:
                continue
            else:
                s_2.append(token)
        s.append(" ".join(s_2))    
        
    return s


def process(review):
    print("original input: ", review)
    df_inp = pd.DataFrame({ 'text': [review] })
    review = clean_desc(df_inp['text'])
    review = tokenization(review)
    review = remove_stopwords(review)

    X_rev_idf = vectorizer.transform(review)
    print("! -- ", X_rev_idf.shape[0] == len(review))
    return X_rev_idf

# ### predict function should return [0] or [1]
#  0 = FAKE  | 1 = FAKE
def predict(review):
    X_rev_idf = process(review)
    print("Processed: ", X_rev_idf)
    prediction = sk_nblearn.predict(X_rev_idf)
    probablity = sk_nblearn.predict_proba(X_rev_idf)
    print('='*30)
    print("results: ")
    print(prediction, probablity, np.max(probablity))
    return {'result':prediction, 'prob':np.max(probablity)}
