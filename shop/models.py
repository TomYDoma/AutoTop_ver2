from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

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

    def return_autopart(self):
        return f"{self.name}, стоимость: {self.price} Р"

    def return_price(self):
        return self.price

    def __str__(self):
        return f"{self.name}, стоимость: {self.price} Р"

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])



class Work(models.Model):
    category = models.ForeignKey(Category, related_name='autopart', null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField('Название работы', max_length=50)
    image = models.ImageField(upload_to='work/%Y/%m/%d', blank=True)
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
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

