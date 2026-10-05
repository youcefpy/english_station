from django.http import HttpResponse
from django.shortcuts import redirect, render

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
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')
    else : 
        form = CoursForm()
    context = { 
        'form': form
        
    }
    return render(request,'cours.html',context=context)