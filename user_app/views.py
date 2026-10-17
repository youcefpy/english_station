import os

from allauth.core.internal.httpkit import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import AdminForm, StudentForm
from .models import Admin, Student


# Create your views here.
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            send_mail(
                subject="Validation email",
                message=f'''
                Hello, a new student has require registration to the plateforme.
                information of students:
                 First name : {student.first_name} \n
                 Last name : {student.last_name} \n
                 Email: {student.email} \n
                 Level acadmy : {student.level}
                 Stram : {student.stream}
                 ''',
                from_email=f"{student.email}",
                recipient_list=[
                    os.getenv('EMAIL_HOST_USER','youcefboutiche@gmail.com'),
                    ],
                fail_silently=True,
            )
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
