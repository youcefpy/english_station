from django.http import HttpRequest
from django.http import HttpResponse
from allauth.core.internal.httpkit import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .forms import AdminForm, StudentForm
from .models import Admin, Student


# Create your views here.
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def login_student(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('index')

    return render(request,'login.html')
