from django.shortcuts import render
from seoul import views

def seoul(request):
    return render(request, 'seoul/seoul.html')
