from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория автозапчастей'
        verbose_name_plural = 'Категории автозапчастей'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_category',
                       args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


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
        return f"{self.name}, цена: {self.price} Р"

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Autopart, self).save(*args, **kwargs)

