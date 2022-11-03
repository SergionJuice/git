from django.contrib import admin

# Register your models here.
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('kat', 'adress', 'kabinet', 'sotrudnik')
admin.site.register(Task, TaskAdmin)

admin.site.register(Kategoria)