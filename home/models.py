from django.db import models
from datetime import datetime
from django.db.models import ImageField
from django.urls import reverse
from django import forms



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

#Обратная связь
class FeedbackList(models.Model):
    name = models.CharField(max_length=200, default = None)
    email = models.CharField(max_length=200, default = None)
    number = models.CharField(max_length=200, default = None)
    date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name



