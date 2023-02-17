import django
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

from django.http import request
from django.urls import reverse

from home.models import SpecialistList, Work

#Дополнение к профилю Django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    numberPhone = models.CharField(default='89999999999', max_length=12)
    bio = models.TextField()
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    class Meta:
        verbose_name = 'Дополнение профиля'
        verbose_name_plural = 'Дополнение профиля'


#Автомобиль
class Car(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    Car_Brand = models.CharField('Марка', max_length=50)
    Car_Model = models.CharField('Модель', max_length=50)
    image = models.ImageField(default='defaultCar.jpg', upload_to='images') #########################
    PTS = models.CharField('ПТС', max_length=50)
    State_Number = models.CharField('Номер', max_length=10)
    VIN = models.CharField('VIN', max_length=20)
    Color = models.CharField('Цвет', max_length=50)
    Relese_Date = models.DateField('Дата выпуска', default=django.utils.timezone.now, null = True)

    def __str__(self):
        return self.VIN

    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'




#Статус заказа
class Status(models.Model):
    Name = models.CharField('Наименование', max_length=50)
    def __str__(self):
        return str(self.Name)
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


#Состав заказа по работам
class CompositionWorks(models.Model):
    Employee = models.ForeignKey(SpecialistList, on_delete=models.CASCADE)
    Works = models.ForeignKey(Work, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Works)
    class Meta:
        verbose_name = 'Состав заказов по работам'
        verbose_name_plural = 'Составы заказов по работам'


#Заказ-наряд
class Order(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Client = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Start_Date = models.DateField('Дата начала', default=django.utils.timezone.now)
    Cost = models.IntegerField('Стоимость')
    CompositionWorks = models.ForeignKey(CompositionWorks, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Car)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'