import django
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

from django.http import request
from django.template.defaultfilters import slugify
from django.urls import reverse


#Дополнение к профилю Django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    numberPhone = models.CharField(default='89999999999', max_length=12)
    middleName = models.CharField(default='Отчество', max_length=40)
    addres = models.CharField(default='Адрес', max_length=200)
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

    def return_photo(self):
        return self.avatar


    class Meta:
        verbose_name = 'Дополнение профиля'
        verbose_name_plural = 'Дополнение профиля'


class TypeCar(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузова'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(TypeCar, self).save(*args, **kwargs)


#Автомобиль
class Car(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )
    Car_Brand = models.CharField('Марка', max_length=50)
    Car_Model = models.CharField('Модель', max_length=50)
    typeCar = models.ForeignKey(TypeCar, related_name='car', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='defaultCar.jpg', upload_to='images')
    PTS = models.CharField('ПТС', max_length=50)
    mileage = models.CharField('Пробег', max_length=10)
    State_Number = models.CharField('Номер', max_length=10)
    VIN = models.CharField('VIN', max_length=20)
    Color = models.CharField('Цвет', max_length=50)
    Relese_Date = models.CharField('Год выпуска', max_length=50)

    def __str__(self):
        return f"{self.Car_Brand} {self.Car_Model}, VIN: {self.VIN}"

    def get_car(self):
        return f"{self.Car_Brand} {self.Car_Model}"

    def get_typeCar(self):
        return f"{self.typeCar.name}"

    def get_stateNumber(self):
        return f"{self.State_Number}"

    def get_Date(self):
        return f"{self.Relese_Date}"

    def get_mileage(self):
        return f"{self.mileage}"

    def get_pts(self):
        return f"{self.PTS}"

    def get_color(self):
        return f"{self.Color}"

    def get_date(self):
        return f"{self.Relese_Date}"

    def get_vin(self):
        return f"{self.VIN}"

    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'




