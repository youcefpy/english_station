from ssl import Options

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
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
def cours_view(request, cours_id):
    if request.method == "POST":
        form = forms.CoursForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else :
        #for admin
        if request.user.is_authenticated and request.user.is_superuser:
            all_cours = Cours.objects.all()
        # for student
        elif request.user.is_authenticated:
            stream = request.user.student.stream
            level = request.user.student.level
            all_cours = Cours.objects.filter(
                id = cours_id,
                stream__name=stream,
                level=level
            )

        form = forms.CoursForm()
    context = {
        'all_cours' : all_cours,
        'form': form
    }
    return render(request,'cours.html',context=context)

@login_required
def stream_view(request):
    # only super user can add stream
    if request.user.is_superuser:
        if request.method == "POST":
                form = forms.StreamForm(request.POST)
                if form.is_valid():
                    form.save()
                return redirect('index')
    if request.user.is_authenticated:
        if request.user.is_superuser:
            all_streams = Stream.objects.all()
        else:
            stream = request.user.student.stream
            level = request.user.student.level
            all_streams = Stream.objects.filter(
                name = stream,
                level = level
            )
    else:
        form = forms.Stream()
    context = {
        "form" : form,
        "streams" : all_streams
    }

    return render(request,'streams.html',context)

@login_required
def unit_view(request):
    form = forms.UnitForm()

    if request.method == "POST" and request.user.is_superuser:
        form = forms.UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("units")

    if request.user.is_superuser:
        all_units = Unit.objects.select_related("stream").prefetch_related("cours_set")
    else:
        student = request.user.student
        student_courses = Cours.objects.filter(
            stream__name=student.stream,
            level=student.level,
        ).select_related("stream")
        all_units = Unit.objects.filter(
            level=student.level,
            stream__name=student.stream,
        ).select_related("stream").prefetch_related(
            Prefetch("cours_set", queryset=student_courses)
        )

    context = {
        "form": form,
        "all_units": all_units,
    }
    return render(request, "units.html", context)

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
