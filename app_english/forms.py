from django import forms
from models import Admin, Cours, Exam, Question, Stream, Student, Unit


class StramForm(forms.ModelForm):
    class Meta: 
        model = Stream
        fields = '__all__'