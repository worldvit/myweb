from django.shortcuts import render,redirect
from .models import Board

# Create your views here.
def index(request):
    a = Board.objects.all()
    context = {
        "blist" : a
    }
    return render(request,'board/index.html',context)


def detail(request,idx):
    a = Board.objects.get(id=idx)
    context = {
        "btitle" : a
    }
    return render(request,'board/detail.html',context)

def delete(request,idx):
    a = Board.objects.get(id=idx)
    a.delete()
    # return render(request,'board/index.html')
    return redirect('index') # 공백 있으면 안됩니다.