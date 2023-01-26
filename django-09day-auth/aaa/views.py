from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def index(request):
    return render(request, 'aaa/index.html')

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

def ulogout(request):
    logout(request)
    return redirect('index')

def profile(request):
    return render(request, 'aaa/profile.html')

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        um = request.POST.get("uemail")
        ul = request.POST.get("uln")
        uf = request.POST.get("ufn")
        # print(un,up,um,ul,uf)
        # User(username=un,
        #      password=up, 암호가 안되면서, 로그인이 안된다.
        #      email=um,
        #      last_name=ul,
        #      first_name=uf).save()
        try:
            User.objects.create_user(
                username=un,
                password=up,
                email=um,
                last_name=ul,
                first_name=uf
            )
        except:
            pass
        return redirect('login')
    return render(request, 'aaa/signup.html')

def delete(request):
    request.user.delete()
    return redirect('index')

def update(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get("uemail")
        ul = request.POST.get("uln")
        uf = request.POST.get("ufn")
        u.email,u.last_name,u.first_name=um,ul,uf
        u.save()
        return redirect('profile')
    return render(request,'aaa/update.html')

def chpass(request):
    if request.method == "POST":
        u = request.user
        cp = request.POST.get("cpass")
        # u.password = cp
        u.set_password(cp)
        u.save()
        return redirect('login')
    return render(request, 'aaa/chpass.html')