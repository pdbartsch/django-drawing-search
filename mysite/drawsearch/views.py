from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Search
from .forms import SearchForm

def home(request):
    if request.method == 'GET':
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
    # if any other method create a blank form
    else:
        form = SearchForm()

    context = {
        'title':'Search Tips & Recommendations',
        'form' : form
    }
    return render(request, 'drawsearch/home.html', context)

def result(request):
    if 'locnum' in request.GET and request.GET['locnum']:
        locnum = request.GET['locnum']
    #eventually include all non null fields
        draws = Search.objects.filter(LocationNumber=locnum).order_by('LocationNumber', '-DrawingNumber', 'SheetNumber')
        resultcount = Search.objects.filter(LocationNumber=locnum).count()
        form = SearchForm(request.GET)
        context = {
            'title':'Results',
            'draws':draws, 
            'resultcount':resultcount, 
            'query':locnum,
            'form':form
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

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'drawsearch/name.html', {'form': form})