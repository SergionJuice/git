from dataclasses import field
from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","adress","kabinet","task"]
        widgets = {
            "title": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите свою проблему'
            })
            }