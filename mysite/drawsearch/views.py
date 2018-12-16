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
    #eventually include all non null fields


    draws = Search.objects.filter(LocationNumber=locnum).order_by('LocationNumber', '-DrawingNumber', 'SheetNumber')
    resultcount = Search.objects.filter(LocationNumber=locnum).count()

    return render(request, 'drawsearch/result.html',
                    {'draws':draws, 'resultcount':resultcount, 'query':locnum})

# can be improved with pop up box or redirect
    # else:
    #     return HttpResponse('Please submit a search term.')

# locnum      locationNumber        LocationNumber
# drawnum     drawingNumber         DrawingNumber
# projtitle   projectTitle          ProjectTitle
# shttitle    sheetTitle            SheetTitle
# shtnum      sheetNumber           SheetNumber
# discp       designDesignation     Discipline
# drawdate    drawingDate           DrawingDate


    # filters = {}
    # if locnum in request.GET and request.GET['locnum']:
    #     filters['LocationNumber'] = locnum
    # if drawnum in request.GET and request.GET['drawnum']:
    #     filters['DrawingNumber'] = drawnum
    # if projtitle in request.GET and request.GET['projtitle']:
    #     filters['ProjectTitle'] = projtitle
    # if shttitle in request.GET and request.GET['shttitle']:
    #     filters['SheetTitle'] = shttitle
    # if shtnum in request.GET and request.GET['shtnum']:
    #     filters['SheetNumber'] = shtnum
    # if discp in request.GET and request.GET['discp']:
    #     filters['Discipline'] = discp
    # if drawdate in request.GET and request.GET['drawdate']:
    #     filters['DrawingDate'] = drawdate

    # draws = Search.objects.filter(**filters)
