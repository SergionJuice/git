from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    ADRESS = (
        ('ШО1', 'ШО1'),
        ('ШО2', 'ШО2'),
        ('ШО8', 'ШО8'),
        ('ШО16', 'ШО16'),
    )
    adress = models.CharField('Корпус',max_length=4, choices=ADRESS)
    kabinet = models.IntegerField('Введите кабинет')
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
