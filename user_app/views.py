import os

from allauth.core.internal.httpkit import redirect
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage, send_mail
from django.db import transaction
from django.shortcuts import render

from .forms import AdminForm, StudentForm
from .models import Admin, Student

# Create your views here.

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.username = student.email
            student.save()
            send_mail(
                subject="Validation email",
                message=(
                    "Hello, a new student has requested registration to the platform.\n"
                    "Student information:\n"
                    f"First name: {student.first_name}\n"
                    f"Last name: {student.last_name}\n"
                    f"Email: {student.email}\n"
                    f"Academic level: {student.level}\n"
                    f"Stream: {student.stream}\n"
                ),
                from_email= student.email,
                recipient_list=[
                    os.getenv(key="EMAIL_HOST_USER")
                ],
            )
            return redirect(to="verification_info")
    else:
        form = StudentForm()
    return render(request, "register.html", {"form": form})

def login_student(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('index')

    return render(request,'login.html')
