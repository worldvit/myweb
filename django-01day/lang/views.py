from django.shortcuts import render

from django.http import HttpResponse
def c(request):
    return HttpResponse("Hello C")

def java(request):
    return HttpResponse("Hello JAVA")

def python(request):
    return HttpResponse("Hello Python")