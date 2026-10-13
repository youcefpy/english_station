from django.shortcuts import render

from .models import Admin, Student


# Create your views here.
def register_student(request):
    context = {}
    return render(request,'register.html',context)

def login_student(request):
    context = {
        'first_name':"Toto",
        "last_name": "Tati"
    }
    return render(request,'login.html',context)
