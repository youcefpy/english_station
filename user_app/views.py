from django.shortcuts import render

from .models import Admin, Student
from .forms import AdminForm, StudentForm

# Create your views here.
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def login_student(request):
    context = {
        'first_name':"Toto",
        "last_name": "Tati"
    }
    return render(request,'login.html',context)
