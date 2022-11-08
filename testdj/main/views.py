from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .forms import TaskForm
from .models import *
from django.contrib.auth import logout
# Create your views here.



def index(request):
    tasks = Task.objects.all()
    return render (request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render (request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена некорректно!'



    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render (request, 'main/create.html',context)

def logout_user(request):
    logout(request)
    return redirect ('home')

