from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

draws = [
    {
        'loc':525,
        'draw':301,
        'title':'library',
        'year':2010
    },
    {
        'loc':534,
        'draw':101,
        'title':'arts',
        'year':2015
    },
    {
        'loc':512,
        'draw':101,
        'title':'bioE',
        'year':2017
    }
]


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
        'draws':draws,
        'title':'Results'
    }
    return render(request, 'drawsearch/result.html', context)