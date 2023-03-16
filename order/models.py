import django
from django.db import models
import accounts.models

####Виды работ
class TypesWork(models.Model):
    name = models.CharField('Название работы', max_length=50)
    price = models.DecimalField('Стоимость',max_digits=10, decimal_places=2)
    execution_Time = models.IntegerField("Срок выполнения")
    warranty = models.IntegerField("Гарантия")


    def __str__(self):
        return f"{self.name}: Р{self.price}"

    def return_price(self):
        return self.price

    def return_work(self):
        return f"{self.name}, стоимость: {self.price} Р"
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
        return f"{self.name}, стоимость: {self.price} Р"

#Статус заказа
class Status(models.Model):
    name = models.CharField('Наименование', max_length=50)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



#Заказ-наряд
class Order(models.Model):
    paid = models.BooleanField(default=False)

    ID_Car = models.ForeignKey(accounts.models.Car, on_delete=models.CASCADE)
    ID_Client = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    work = models.ManyToManyField(TypesWork)

    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created}, Р{self.total_price()}: {self.paid}"

    def total_price(self):
        i = 0
        for cart_item in self.work.all():
            i += cart_item.return_price()
        return sum([
            cart_item.total()
            for cart_item in OrderAutopart.objects.filter(order=self)
        ], i)

    def total_work(self):
        return ([
            cart_item.return_work()
            for cart_item in self.work.all()
        ])
    def total_autopart(self):
        return ([
            cart_item.return_autopart()
            for cart_item in OrderAutopart.objects.filter(order=self)
        ])


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderAutopart(models.Model):
    autopart = models.ForeignKey(Autopart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    def total(self):
        return self.count * self.autopart.price

    def return_autopart(self):
        return f"{self.autopart}, Количество: {self.count} ШТ"
    def __str__(self):
        return f"{self.autopart.name}, " \
               f"р{self.autopart.price} * {self.count} = Р{self.total()}"