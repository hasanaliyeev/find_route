import datetime

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class Person(models.Model):
    dt_now = datetime.datetime.now()
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    city = models.CharField(max_length=100, verbose_name='Город')
    birth_date = models.DateField(verbose_name='День рождения')
    reg_date = dt_now

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
