from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def seoul(request):
    return HttpResponse("Hello Seoul")