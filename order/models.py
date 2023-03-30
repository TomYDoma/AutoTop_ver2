from datetime import datetime

from django.urls import reverse
from django.db import models
import accounts.models
import work.models

import shop.models



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
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    ID_Car = models.ForeignKey(accounts.models.Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    ID_Client = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Клиент')

    car_mileage = models.IntegerField(verbose_name='Пробег')
    client_date = models.DateField('Желаемая дата для клиента', default=datetime.now)
    client_time = models.TimeField('Желаемое время для клиента', default=datetime.now)

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Заказ от: {self.created.strftime('%d.%m.%Y-%H.%M')}, заказчик: {self.ID_Client.last_name} {self.ID_Client.first_name}"

    def total_work(self):
        return ([
            cart_item.return_work()
            for cart_item in OrderWork.objects.filter(order=self)
        ])


    def total_autopart(self):
        return ([
            cart_item.return_autopart()
            for cart_item in OrderItem.objects.filter(order=self)
        ])

    def total_autopart_to_string(self):
        return f'{Order.total_autopart(self)}'

    def return_car_milage(self):
        return f'{self.car_mileage} километров'


    def return_paid(self):
        if self.paid == True:
            return "Оплачено"
        else:
            return "Не оплачено"

    def get_absolute_url(self):
        return reverse('order:order_detail', args=[str(self.id)])


    def total_price(self):
        i = 0
        for cart_item in OrderWork.objects.filter(order=self):
            i += cart_item.return_price()
        j = 0
        for cart_item in OrderItem.objects.filter(order=self):
            j += cart_item.return_price()
        return sum([j, i])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(shop.models.Autopart, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product}, "

    def return_price(self):
        return self.product.price * self.quantity

    def return_autopart(self):
        return f"{self.product}, количество: {self.quantity}, стоимость: {self.product.price * self.quantity} рублей"

    def total(self):
        return self.quantity * self.product.price

class OrderWork(models.Model):
    order = models.ForeignKey(Order, related_name='work', on_delete=models.CASCADE)
    work = models.ForeignKey(work.models.Work, related_name='order_work', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.work}, "

    def return_price(self):
        return self.work.price


    def return_work(self):
        return f"{self.work}, стоимость: {self.work.price} рублей"





