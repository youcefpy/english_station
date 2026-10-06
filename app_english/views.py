from django.http import HttpResponse
from django.shortcuts import redirect, render

from app_english.models import Cours

from .forms import CoursForm

# Create your views here.


def index(request):
    context = {
        'admin': 'Bouchra'
    }
    return render(request,'index.html',context=context)


#login required for student and admin
def form_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else : 
        all_cours = Cours.objects.all() 
        form = CoursForm()
    context = { 
        'all_cours' : all_cours,
        'form': form
        
    }
    return render(request,'cours.html',context=context)
