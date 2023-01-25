from django.shortcuts import render
from .models import Teacher

# Create your views here.
def index(request):
    a = Teacher.objects.all()

# html에서 변수로 사용할 수 있다. 
    context = {
        "tlists": a,
    }
    return render(request,"testdb/index.html", context)