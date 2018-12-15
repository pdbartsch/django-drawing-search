from django.shortcuts import render
from django.http import HttpResponse

from .models import Search

#improve by switching to django forms
# from .forms import SearchForm

def home(request):
    context = {
        'title':'Search Tips & Recommendations',
    }
    return render(request, 'drawsearch/home.html', context)


def result(request):
    context = {
        # 'draws':draws,
        # 'draws': Search.objects.filter(LocationNumber = 525),
        'title':'Results'
    }
    return render(request, 'drawsearch/result.html', context)

def search_form(request):
    return render(request, 'drawsearch/search_form.html')

def search(request):
    if 'locnum' in request.GET and request.GET['locnum']:
        locnum = request.GET['locnum']
        draws = Search.objects.filter(LocationNumber=locnum)
        resultcount = Search.objects.filter(LocationNumber=locnum).count()

        #eventually include all non null fields

        # filters = {}
        # if LocationNumber:
        #     filters['LocationNumber'] = LocationNumber
        # if DrawingNumber:
        #     filters['DrawingNumber'] = DrawingNumber

        # draws = Search.objects.filter(**filters)

        return render(request, 'drawsearch/result.html',
                      {'draws': draws, 'resultcount':resultcount, 'query': locnum})

# can be improved with pop up box or redirect
    else:
        return HttpResponse('Please submit a search term.')
