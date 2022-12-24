from django.db import models
from datetime import datetime
from django.db.models import ImageField
from django.urls import reverse
from django import forms
from django.utils.safestring import mark_safe


class SpecialistAdmin(models.Model):
    name = models.CharField(max_length=200)
    positions = models.CharField(max_length=200, default = None)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __repr__(self):
        return 'Image(%s, %s)' % (self.name, self.positions, self.image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

class SpecialistList(models.Model):
    name = models.CharField(max_length=200)
    positions = models.CharField(max_length=200, default = None)
    WorkExperience = models.IntegerField(default = None)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __repr__(self):
        return 'Image(%s, %s)' % (self.name, self.positions, self.image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалисты'

#Таблица с записями на главной странице
class mainCart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __repr__(self):
        return 'Image(%s, %s)' % (self.name, self.positions, self.image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная станица - Карточки'
        verbose_name_plural = 'Главная станица - Карточки'

#Обратная связь
class FeedbackList(models.Model):
    name = models.CharField(max_length=200, default = None)
    email = models.CharField(max_length=200, default = None)
    number = models.CharField(max_length=200, default = None)
    date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField(upload_to='images/', null=True)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Содеражние')
    date = models.DateTimeField('Дата публицации')

    def __str__(self):
        return self.title

    def display_my_safefield(self):
        return mark_safe(self.anons)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'