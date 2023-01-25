from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jeju(request):
    # return HttpResponse("Hello Jeju")
    return render(request,'jeju.html')