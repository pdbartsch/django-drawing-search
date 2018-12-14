from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm

def home(request):
    context = {
        'title':'Search Tips & Recommendations'
    }
    return render(request, 'drawsearch/home.html', context)


def result(request):
    context = {
        # 'draws':draws,
        'draws': Search.objects.filter(LocationNumber = 525),
        'title':'Results'
    }
    return render(request, 'drawsearch/result.html', context)