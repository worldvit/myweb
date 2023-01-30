from django.shortcuts import render


def home(request):
    return render(request, 'local/home.html')
def jeju(request):
    return render(request, 'local/jeju.html')
def seoul(request):
    return render(request, 'local/seoul.html')