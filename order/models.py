import django
from django.db import models

import accounts.models
import home



####Виды работ
class TypesWork(models.Model):
    Name = models.CharField('Название работы', max_length=50)
    Price = models.DecimalField('Стоимость',max_digits=10, decimal_places=2)
    Execution_Time = models.IntegerField("Срок выполнения")
    Warranty = models.IntegerField("Гарантия")
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

####Категории запчастей
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

####Запчасти
class Autopart(models.Model):
    category = models.ForeignKey(Category, related_name='autopart', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='autopart/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Автозапчасть'
        verbose_name_plural = 'Автозапчасти'

    def __str__(self):
        return self.name


####Состав заказа
class CompositionOrder(models.Model):
    #ID_Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ID_TypesWorks = models.ManyToManyField(TypesWork)
    ID_Employee = models.ForeignKey(home.models.SpecialistList, on_delete=models.PROTECT)
    ID_Autopart = models.ManyToManyField(Autopart)

    def __str__(self):
        return str(self.ID_TypesWorks)
    class Meta:
        verbose_name = 'Состав заказов'
        verbose_name_plural = 'Составы заказов'


#Статус заказа
class Status(models.Model):
    Name = models.CharField('Наименование', max_length=50)
    def __str__(self):
        return str(self.Name)
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


#Заказ-наряд
class Order(models.Model):
    ID_Car = models.ForeignKey(accounts.models.Car, on_delete=models.CASCADE)
    ID_Client = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ID_CompositionOrder = models.ForeignKey(CompositionOrder, on_delete=models.PROTECT)
    Status = models.ForeignKey(Status, on_delete=models.PROTECT)
    Start_Date = models.DateTimeField(auto_now_add=True)
    End_Date = models.DateTimeField(auto_now=True)
    Cost = models.IntegerField('Стоимость')

    def __str__(self):
        return str(self.Start_Date)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



