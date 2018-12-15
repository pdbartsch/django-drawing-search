from django.shortcuts import render
from django.http import HttpResponse

from .models import Search
# from .forms import SearchForm

def home(request):
    context = {
        'title':'Search Tips & Recommendations',
    }
    return render(request, 'drawsearch/home.html', context)


def result(request):
    context = {
        # 'draws':draws,
        'draws': Search.objects.filter(LocationNumber = 525),
        'title':'Results'
    }
    return render(request, 'drawsearch/result.html', context)

    
def search_form(request):
    return render(request, 'drawsearch/search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        draws = Search.objects.filter(projtitle__icontains=q)
        return render(request, 'drawsearch/search_results.html',
                      {'draws': draws, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

# locnum 
# drawnum
# projtitle
# shttitle 
# shtnum
# discp
# drawdate 
