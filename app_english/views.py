from django.http import HttpResponse
from django.shortcuts import redirect, render

import app_english.forms as forms
from app_english.models import Cours, Stream

# Create your views here.


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