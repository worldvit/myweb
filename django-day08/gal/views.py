from django.shortcuts import render,redirect
from .models import gallery

# Create your views here.
def index(request):
    a = gallery.objects.all()
    context = { "ilist" : a }
    
    return render(request, 'gal/index.html',context)

def create(request):
    # if request.method == "POST":
    gn = request.POST.get("gname")
    gi = request.FILES.get("gimage")
    gm = request.POST.get("gmemo")
    
    gallery(name=gn,image=gi,memo=gm).save()
    
    return redirect('index')

def delete(request,idx):
    a = gallery.objects.get(id=idx)
    a.image.delete()
    a.delete()
    return redirect('index')