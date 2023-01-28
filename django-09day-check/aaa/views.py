from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password

# Index Function
def index(request):
    return render(request, 'aaa/index.html')

# Ulogin Function
def ulogin(request): # 함수이름이 login이면 안됨.
    if request.method == "POST":
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")
        # print(authenticate(username=uname, password=upass)) #일치하면 id, 없으면 none
        udb = (authenticate(username=uname, password=upass))
        if udb:
            login(request, udb)
            return redirect('index')
        else:
            pass
    return render(request, 'aaa/login.html')

# Ulogout Function
def ulogout(request):
    logout(request)
    return redirect('index')

# Profile Function
def profile(request):
    return render(request, 'aaa/profile.html')

# Signup Function
def signup(request):
    if request.method == "POST":
        ui = request.FILES.get("uimage")
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        um = request.POST.get("uemail")
        ul = request.POST.get("uln")
        uf = request.POST.get("ufn")
        uc = request.POST.get("ucom")
        ua = request.POST.get("uage")
        
        try:
            User.objects.create_user(
                pic = ui,
                username=un,
                password=up,
                email=um,
                last_name=ul,
                first_name=uf,
                comment=uc,
                age=ua,
            )
            User(pic=ui).save()
        except:
            pass
        return redirect('login')
    return render(request, 'aaa/signup.html')

# Delete Function
def delete(request):
    request.user.pic.delete()
    request.user.delete()
    return redirect('index')

# Update Function
def update(request):
    if request.method == "POST":
        u = request.user
        ui = request.FILES.get("uimage")
        um = request.POST.get("uemail")
        ul = request.POST.get("uln")
        uf = request.POST.get("ufn")
        uc = request.POST.get("ucom")
        ua = request.POST.get("uage")
        # u.email,u.last_name,u.first_name,u.pic,u.comment,u.age=um,ul,uf,ui,uc,ua
        u.email=um
        u.last_name=ul
        u.first_name=uf
        u.comment=uc
        u.age=ua
        if ui:
            u.pic.delete()
            u.pic = ui
        u.save()
        return redirect('profile')
    return render(request,'aaa/update.html')

# Chpass Function
def chpass(request):
    if request.method == "POST":
        u = request.user
        cp = request.POST.get("cpass")
        if check_password(cp,u.password):
            np = request.POST.get("npass")
            u.set_password(np)
            u.save()
            return redirect('login')
    return render(request, 'aaa/chpass.html')
