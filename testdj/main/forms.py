from dataclasses import field
from distutils.text_file import TextFile
from .models import Task
from django.forms import ModelForm, TextInput, Textarea,IntegerField, CharField, Select

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","adress","kabinet","task","sotrudnik"]
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     #for field in self.fields:
        #         #self.fields[field].widget.attrs['autocomplete'] = 'off'
        #     self.fields['title'].widget.attrs['placeholder' == 'Введите свою проблему','class' : 'form-control',] = 'Your first name'
        #     self.fields['adress'].widget.attrs['placeholder'] = 'Your last name'
        #     self.fields['kabinet'].widget.attrs['placeholder'] = 'Your age'
        #     self.fields['task'].widget.attrs['placeholder'] = 'Your username'




        widgets = {
            "title": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите свою проблему'
            }),
            "adress": Select(
                 attrs={
                  'name' : 'Выберите корпус',
                  'required' : 'required',
                  'class' : 'form-control'
             }
            ),
            "kabinet" : TextInput(
                attrs={
                'type' : 'number',
                'placeholder' : 'Кабинет' ,
                'class' : 'form-control',
                'max' : '339',
                'required' : 'required'
            
            }
            ),
            "task" : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите описание проблемы'
            }),
            "sotrudnik": Select(
                 attrs={
                  'name' : 'Желаемый сотрудник',
                  'required' : 'required',
                  'class' : 'form-control'
             }
            ),
        }