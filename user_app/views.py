import os

from allauth.core.internal.httpkit import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from user_app.services import send_password_setup_email

from .forms import StudentForm, StudentFormSetPassWord
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
    """ 
        set password to the user after acceptence of the admin (Teacher)
        we need to filter by email. The email is unique
    """
    if request.method == "POST":
        form= StudentFormSetPassWord(request.POST)

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
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('index')

    return render(request,'login.html')

@staff_member_required
@require_POST
def approve_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if not student.is_active:
        student.is_active = True
        student.save(update_fields=["is_active"])
        send_password_setup_email(student, request)

    return redirect("admin_page")

def admin_page(request):
    students = Student.objects.all()
    context = {
        'students':students
    }

    return render(request, 'admin_page.html', context= context)
