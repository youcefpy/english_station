from django import forms

from .models import Cours, Exam, Question, Stream, Unit


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = '__all__'  # noqa: DJ007

class CoursForm(forms.ModelForm):
    class Meta:
        model=Cours
        fields = '__all__'  # noqa: DJ007

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"  # noqa: DJ007

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields = '__all__'  # noqa: DJ007
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"  # noqa: DJ007
