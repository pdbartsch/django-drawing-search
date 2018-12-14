from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm

def home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'drawsearch/search.html', context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request, 'drawsearch/about.html', context)

def result(request):
    context = {
        # 'draws':draws,
        'draws': Search.objects.filter(LocationNumber = 525),
        'title':'Results'
    }
    return render(request, 'drawsearch/result.html', context)