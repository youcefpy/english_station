import os

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.http import require_POST

from user_app.services import send_password_setup_email

from .forms import StudentForm, StudentFormSetPassWord, StudentLogin
from .models import Student

# Create your views here.

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.username = student.email
            student.is_active = False
            student.set_unusable_password()
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
                recipient_list = [
                    os.getenv(key="EMAIL_HOST_USER", default="youcefboutiche28@gmail.com")
                ],
            )
            return redirect(to="verification_info")
    else:
        form = StudentForm()
    return render(request, "register.html", {"form": form})

def set_password_student(request, uidb64, token):
    try:
        student_id = force_str(urlsafe_base64_decode(uidb64))
        print(f"student_id ===> {student_id}")
        student = get_object_or_404(Student, pk=student_id)
    except (TypeError, ValueError, OverflowError):
        return render(request, template_name = "set_password.html",
        context={
            "error": "This password setup link is invalid or expired."
        },
        status=400)

    if not default_token_generator.check_token(student, token):
        return render(request, "set_password.html", context={
            "error": "This password setup link is invalid or expired."
        },
        status=400
        )

    if request.method == "POST":
        form = StudentFormSetPassWord(request.POST, instance=student)

        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(form.cleaned_data["password"])
            student.save()
            return redirect('login')
    else:
        form = StudentFormSetPassWord()
    context = {
        'form':form
    }

    return render(request,'set_password.html', context=context)


def login_student(request):
    if request.method == "POST":
        form = StudentLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
    else:
        form = StudentLogin()
    context = {
        'form':form
    }
    return render(request,template_name='login.html',context=context)

@require_POST
def logout_student(request):
    logout(request)
    return redirect(to='login')

@staff_member_required
@require_POST
def approve_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if not student.is_active:
        student.is_active = True
        student.save(update_fields=["is_active"])
        send_password_setup_email(student, request)

    return redirect("admin_panel")

@staff_member_required
def admin_page(request):
    students = Student.objects.all()
    context = {
        'students':students,
    }
    return render(request, 'admin_panel.html', context= context)
