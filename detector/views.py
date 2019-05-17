from django.shortcuts import render
from .forms import ReviewForm
from ml import model as ml
# from django.http import HttpResponse
# Create your views here.

# results = [
#     {
#         'pred': True,
#         'acc': "80%"
#     },
#     {
#         'pred': False,
#         'acc': "70%"
#     }
# ]

def home(request):
    results=""

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.data['text']
        result = ml.predict(review)
        print("result: ", result['result'])
        print("prob: ", result['prob'])

        if result['result'] == 0:
            results = 'Given review is Not fake'
        else:
            results = "Given review is Fake"
        prob_statement = "probablity score: "+str(result['prob'])

        context = {
        'form': form,
        'results': results,
        'prob': prob_statement
        }
        
        return render(request, 'detector/home.html', context=context)

    else:
        form = ReviewForm()
        return render(request, 'detector/home.html', {'form': form})
    
    

