from django import forms

from .models import Admin, Cours, Exam, Question, Stream, Student, Unit


class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = '__all__'

class StreamForm(forms.ModelForm):
    class Meta: 
        model = Stream
        fields = '__all__'

class CoursForm(forms.ModelForm):
    class Meta:
        model=Cours
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields = '__all__'
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"