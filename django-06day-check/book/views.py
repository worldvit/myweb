from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    a = Book.objects.all()
    
    context = {
        "sites" : a,
    }    
    return render(request, 'book/index.html',context)

def detail(request,idx):
    a = Book.objects.get(id=idx)
    context = {
        "abook" : a,
    }
    return render(request,'book/detail.html',context)