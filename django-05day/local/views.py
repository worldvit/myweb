from django.shortcuts import render


def jeju(request):
    return render(request, 'local/jeju.html')
def seoul(request):
    return render(request, 'local/seoul.html')