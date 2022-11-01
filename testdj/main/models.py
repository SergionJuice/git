from logging import PlaceHolder
from random import choices
from django.db import models

# Create your models here.

class Task(models.Model):
    kat = models.ForeignKey('Kategoria', on_delete=models.PROTECT,null=False)
    title = models.CharField('Название', max_length = 50)
    ADRESS = (
        ('ШО1', 'ШО1'),
        ('ШО2', 'ШО2'),
        ('ШО8', 'ШО8'),
        ('ШО16', 'ШО16'),
    )
    blank_choice = (('', 'Выберите корпус'),)
    adress = models.CharField('Корпус',max_length=4,choices=blank_choice + ADRESS)
    kabinet = models.IntegerField('Введите кабинет')
    task = models.TextField('Описание')
    
    SOTRUDNIK = (
        ('AA', 'Артем Андреевич'),
        ('YI', 'Ярослав Игоревич'),
        ('SV', 'Сергей Викторович'),
        ('NO', 'Никита Олегович'),
    )
    sotrudnik_choice = (('', 'Выберите сотрудника'),)
    sotrudnik = models.CharField('Сотрудник',max_length=2,choices=sotrudnik_choice + SOTRUDNIK)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Kategoria(models.Model):
    KATEGORIA =(
        ('Замена Картриджа','Замена Картриджа'),
        ('Устранение неполадок с техникой','Устранение неполадок с техникой'),
        ('Выдача оборудования','Выдача оборудования'),
        ('Другое','Другое'),
    )
    kategoria_choice = (('', 'Выберите категорию обращения'),)
    kategoria = models.CharField('Категория',max_length=50,choices=kategoria_choice + KATEGORIA, db_index=True)
    def __str__(self):
        return self.kategoria
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
