from django.shortcuts import render

# Create your views here.
def block(request):
    return render(request, 'block/block.html')