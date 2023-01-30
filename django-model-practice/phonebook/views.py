from django.shortcuts import render
from .models import Phonebook

# Create your views here.
# def index(request):
#     return render(request,'PBook/index.html')
def index(request):
    members = Phonebook.objects.all()
    context={'Phonebook' : members} # 공백 중요
    return render(request,'PBook/index.html',context)

def add(request):
    return render(request,'PBook/add.html')

def delete(request):
    return render(request,'PBook/delete.html')

def detail(request,idx):
    userinfo = Phonebook.objects.values('id','fname','lname','address','email','phone','birthday').get(id=idx)
    context={ 'Phonebook' : userinfo }
    return render(request,'PBook/detail.html',context)

def update(request):
    return render(request,'PBook/update.html')