from django.shortcuts import render,redirect
from .models import Teachers

# Create your views here.
def index(request):
    a = Teachers.objects.all()
    context = { "tlist" : a }
    return render(request, 'teachers/index.html',context)

def detail(request,idx):
    a = Teachers.objects.get(id=idx)
    context = { "tlist" : a }
    return render(request, 'teachers/detail.html',context)

def delete(request,idx):
    a = Teachers.objects.get(id=idx)
    a.delete()
    return redirect('index')

def create(request):
    if request.method == 'POST':
        tfna = request.POST.get("fna")
        tlna = request.POST.get("lna")
        tnna = request.POST.get("nna")
        tage = request.POST.get("age")
        tpho = request.POST.get("pho")
        tadd = request.POST.get("add")
        tmem = request.POST.get("mem")
        Teachers(
            fname=tfna,
            lname=tlna,
            nname=tnna,
            age=tage,
            phone=tpho,
            address=tadd,
            memo=tmem
            ).save()
        return redirect('index')
    return render(request, 'teachers/create.html')

def update(request,idx):
    a = Teachers.objects.get(id=idx)
    print(a.fname)
    if request.method == "POST":
        tfna = request.POST.get("fna")
        tlna = request.POST.get("lna")
        tnna = request.POST.get("nna")
        tage = request.POST.get("age")
        tpho = request.POST.get("pho")
        tadd = request.POST.get("add")
        tmem = request.POST.get("mem")
        
        a.fname = tfna
        a.lname = tlna
        a.nname = tnna
        a.age = tage
        a.address = tadd
        a.phone = tpho
        a.memo = tmem
        a.save()
        return redirect("detail", idx)
    context = { "tlist" : a }
    return render(request, 'teachers/update.html',context)