from django.shortcuts import render,redirect
from .models import Shop

# Create your views here.
def index(request):
    a = Shop.objects.all()
    context = { "slist" : a } 
    return render(request, 'shop/index.html',context)
def detail(request,idx):
    a = Shop.objects.get(id=idx)
    context = { "stitle" : a }
    return render(request, "shop/detail.html",context)
def delete(request,idx):
    a = Shop.objects.get(id=idx)
    a.delete()
    return redirect("index")
def create(request):
    if request.method == "POST":
        sn = request.POST.get("sname")
        sp = request.POST.get("sprice")
        sc = request.POST.get("scon")
        # print(sn,sp,sc)
        Shop(name=sn, price=sp, content=sc, likey=0).save()
        return redirect("index")
    return render(request, "shop/create.html")
def update(request,idx):
    a = Shop.objects.get(id=idx)
    
    if request.method == "POST":
        sn = request.POST.get("sname")
        sp = request.POST.get("sprice")
        sc = request.POST.get("scon")
        a.name,a.price,a.content = sn,sp,sc
        a.save()
        return redirect("detail", idx)
    context= {"stitle" : a }
    return render(request, "shop/update.html",context)
# def test(request):
#     print(request.method)
#     # print(request.GET)
#     # print(request.GET.get("var1"))
#     # print(request.GET.get("var2"))
#     print(request.POST)
#     print(request.POST.get("var1"))
#     print(request.POST.get("var2"))
#     return render(request, "shop/test.html")