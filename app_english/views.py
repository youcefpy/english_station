from django.http import HttpResponse
from django.shortcuts import render

from .forms import CoursForm

# Create your views here.


def index(request):
    context = {
        'admin': 'Bouchra'
    }
    return render(request,'index.html',context=context)


#login required
def form_cours(request):
    if request.method == "POST":
        ...

    context = { 
        
    }
    return render(request,'cours.html',context=context)