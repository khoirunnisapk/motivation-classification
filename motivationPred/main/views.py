from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from model.motivation_classification import predict

def index(request):
    context={'a': 'Hello'}
    return render(request, 'index.html', context)


def classifyMotivation(request):
    print(request.POST.get('value'))
    sentence = request.POST.get('value')
    result = predict(sentence)
    print("ini result ", result)
    context={'a':'Helloworld'}
    return render(request, 'index.html', context)