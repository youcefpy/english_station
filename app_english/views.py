from ssl import Options

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app_english import forms
from app_english.models import Cours, Exam, Question, Stream, Unit


# Create your views here.
def check_information_student_view(request):

    context = {

    }
    return render(request,'checking_signup.html',context)

@login_required
def index(request):
    context = {

    }
    return render(request,'index.html',context=context)


#login required for student and admin
@login_required
def cours_view(request,stream=None):
    if request.method == "POST":
        form = forms.CoursForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else :
        #for admin
        if request.user.is_authenticated and request.user.issuperuser:
            all_cours = Cours.objects.all()
        elif request.user.is_authenticated:
            all_cours = Cours.objects.filter(stream=stream)

        form = forms.CoursForm()
    context = {
        'all_cours' : all_cours,
        'form': form
    }
    return render(request,'cours.html',context=context)

@login_required
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

@login_required
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

@login_required
def exam_view(request):
    if request.method == "POST":
        form = forms.ExamForm(request.POST)

        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_exams = Exam.objects.all() # this is not correct we need to filter
        #exams by stream and by acadimic level
        form = forms.ExamForm()
    context = {
        'form' : form,
        'all_exams' : all_exams # same here we dont need to get all exams

    }
    return render(request,"exam.html",context)

@login_required
def question_view(request):
    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_questions = Question.objects.all() # this is not correct we need to filter
        #exams by stream and by acadimic level
        form = forms.QuestionForm()
    context = {
        'form' : form,
        'all_questions' : all_questions
    }
    return render(request,"question.html",context)
@login_required
def options_view(request):
    if request.method == "POST":
        form = forms.OptionsForm(request.POST)

        if form.is_valid():
            form.save()
        return render("index")
    else:
        all_options = Options.objects.all() # this is not correct we need to filter
        #exams by stream and by acadimic level
        form = forms.OptionsForm()
    context = {
        'form' : form,
        'all_options' : all_options
    }
    return render(request,"question.html",context)
