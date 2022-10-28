from django.shortcuts import render

from .forms import TaskForm
from .models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render (request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render (request, 'main/about.html')

def create(request):
    form = TaskForm
    context = {
        'form': form
    }
    return render (request, 'main/create.html',context)