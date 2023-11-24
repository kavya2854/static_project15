from django.shortcuts import render

# Create your views here.
def tables(request):
    return render(request,'tables.html')

def inlinestylesheet(request):
    return render(request,'inlinestylesheet.html')

def external(request):
    return render(request,'external.html')

def idselector(request):
    return render(request,'idselector.html')

def pseudoselector(request):
    return render(request,'pseudoselector.html')

def forms(request):
    return render(request,'forms.html')

def combinators(request):
    return render(request,'combinators.html')

def index(request):
    return render(request,'index.html')

def absolute(request):
    return render(request,'absolute.html')

def transforms(request):
    return render(request,'transforms.html')