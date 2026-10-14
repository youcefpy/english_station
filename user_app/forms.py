from dataclasses import fields
from django.forms import ModelForm
from .models import Student, Admin


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','level','stream']

class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
