from django.shortcuts import render
from django.http import HttpResponse

from .models import Search
from .forms import SearchForm

def home(request):
    form = SearchForm()
    context = {
        'title':'Search Tips & Recommendations',
        'form':form,
    }
    return render(request, 'drawsearch/home.html', context)

def result(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        # process the data in form.cleaned_data
        locnum = form.cleaned_data['locnum']
        drawnum = form.cleaned_data['drawnum']
        projtitle = form.cleaned_data['projtitle']
        shttitle = form.cleaned_data['shttitle']
        shtnum = form.cleaned_data['shtnum']
        discp = form.cleaned_data['discp']
        drawdate = form.cleaned_data['drawdate']

        # Only include fields that have a value meaning the user has searched by that field
        filters = {}
        if locnum:
            filters['LocationNumber'] = locnum
        if drawnum:
            filters['DrawingNumber'] = drawnum
        if projtitle:
            filters['ProjectTitle'+'__contains'] = projtitle
        if shttitle:
            filters['SheetTitle'+'__contains'] = shttitle
        if shtnum:
            filters['SheetNumber'+'__contains'] = shtnum
        if discp:
            filters['Discipline'+'__contains'] = discp
        if drawdate: #greater than or equal to
            filters['DrawingDate'+'__gte'] = drawdate

        draws = Search.objects.filter(**filters).order_by('LocationNumber', '-DrawingNumber', 'SheetNumber')
        resultcount = Search.objects.filter(**filters).count()
        context = {
            'title':'Results',
            'draws':draws, 
            'resultcount':resultcount, 
            'form':form,
            'filters':filters
        }
    else:
        form = SearchForm()
        context = {
            'form':form,
        }
    return render(request, 'drawsearch/result.html', context)

# locnum      locationNumber        LocationNumber
# drawnum     drawingNumber         DrawingNumber
# projtitle   projectTitle          ProjectTitle
# shttitle    sheetTitle            SheetTitle
# shtnum      sheetNumber           SheetNumber
# discp       designDesignation     Discipline
# drawdate    drawingDate           DrawingDate
