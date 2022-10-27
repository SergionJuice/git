from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    ADRESS = (
        ('1', 'ШО1'),
        ('2', 'ШО2'),
        ('8', 'ШО8'),
        ('16', 'ШО16'),
    )
    adress = models.CharField('Корпус',max_length=4, choices=ADRESS)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
