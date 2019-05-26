# yelp-fake-reviews-detector
A machine learning system to detect fake reviews on Yelp.

## Demo:
<img src="pics/app_demo.gif"/>

## Model training
Refer to the <a href="">Jupyter notebooks</a> in research folder to know the steps taken for preprocessing, model development and algorithms used.
Alghough we experemented with different models, we found Naive Bayes to be most accurate with F1 score of 77%.
<img src="pics/nb_roc.png/>

## Installing and running this app:
1. Requirements:
Use pip install/conda install to download following packages
  - Numpy, pandas
  - sklearn
  - spacy
  - Django 2.1
  - pickle
  - tqdm
  
 2. running the app:
  - Go to folder containing manage.py and run command: python manage.py runserver
  - Once the server starts, open browser. The app runs on http://127.0.0.1:8000/
  - fake_reviews.txt and real_reviews.txt contains some reviews that can be used to test the working of model.
  
