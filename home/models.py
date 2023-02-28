import django
from django.db import models
from datetime import datetime
from django.urls import reverse
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
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

#Таблица с записями на главной странице
class mainCart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    date = models.DateTimeField(default=django.utils.timezone.now)
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
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    email = models.CharField(max_length=200, default = None)
    number = models.CharField(max_length=200, default = None)
    date = models.DateTimeField(default=django.utils.timezone.now)
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


class Comment(models.Model):
    article = models.ForeignKey(
        'Articles',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=django.utils.timezone.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("comment", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


