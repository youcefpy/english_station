from django.http import HttpResponse
from django.shortcuts import redirect, render

import app_english.forms as forms
from app_english.models import Cours, Exam, Question, Stream, Unit

# Create your views here.


def admin_view(request):
    ...

    
def student_view(request):
    ...



def index(request):
    context = {
        'admin': 'Bouchra'
    }
    return render(request,'index.html',context=context)


#login required for student and admin
def cours_view(request):
    if request.method == "POST":
        form = forms.CoursForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else : 
        all_cours = Cours.objects.all() 
        form = forms.CoursForm()
    context = { 
        'all_cours' : all_cours,
        'form': form
        
    }
    return render(request,'cours.html',context=context)


def stream_view(request):
    if request.method == "POST":
        form = forms.StreamForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else : 
        all_streams = Stream.objects.all()
        form = forms.Stream()
    context = {
        "form" : form,
        "stream" : all_streams
    }

    return render(request,'stream.html',context)

def unit_view(request):
    if request.method == "POST":
        form = forms.UnitForm(request.POST)

        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_units = Unit.objects.all()
        form = forms.UnitForm()
    context = {
        'form' : form,
        'all_units' : all_units
    }
    return render(request,"unit.html",context)

def exam_view(request):
    """
    """
    if request.method == "POST":
        form = forms.ExamForm(request.POST)

        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_exams = Exam.objects.all() # this is not correct we need to filter exams by stream and by acadimic level
        form = forms.ExamForm()
    context = {
        'form' : form,
        'all_exams' : all_exams # same here we dont need to get all exams 

    }
    return render(request,"exam.html",context)

def question_view(request):
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)

        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_exams = Question.objects.all() # this is not correct we need to filter exams by stream and by acadimic level
        form = forms.QuestionForm()
    context = {
        'form' : form,
        'all_units' : all_exams
    }
    return render(request,"question.html",context)