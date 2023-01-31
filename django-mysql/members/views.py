from django.shortcuts import render,redirect
from .models import Members

# Create your views here.
def members(request):
    mlist = Members.objects.all().order_by('-id')
    return render(request, 'members/index.html',{ "mlist" : mlist} )