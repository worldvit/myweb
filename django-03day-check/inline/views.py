from django.shortcuts import render

# Create your views here.
def inline(request):
    return render(request, 'inline/inline.html')