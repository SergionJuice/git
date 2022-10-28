from dataclasses import field
from .models import Task
from django.forms import ModelForm, TextInput, CharField,IntegerField,TextField

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","adress","kabinet","task"]
        widgets = {
            "title": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите свою проблему'
            }),
            "adress": CharField(attrs={
                'name' : 'Выберите корпус',
                'required' : 'required',
                'class' : 'form-control'
            }),
            "kabinet" : IntegerField(attrs={
                'placeholder' : 'Кабинет' ,
                'class' : 'form-control',
                'max' : '339',
                'required' : 'required'
            
            }),
            "task" : TextField(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите описание проблемы'
            })
            }