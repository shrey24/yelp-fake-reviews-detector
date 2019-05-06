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
        print("result: ", result)
        print(result.shape)

        if result[0] == 0:
            results = 'Not fake'
        else:
            results = "Fake"

    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'results': results
    }
    
    return render(request, 'detector/home.html', context=context)

