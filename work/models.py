from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class CategoryWork(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CategoryWork, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('work:work_list_by_category',
                       args=[self.slug])



class Work(models.Model):
    category = models.ForeignKey(CategoryWork, related_name='work', null=True, on_delete=models.SET_NULL)
    name = models.CharField('Название работы', max_length=50)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='work/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField('Стоимость',max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    execution_Time = models.IntegerField("Срок выполнения")
    warranty = models.IntegerField("Гарантия")

    def __str__(self):
        return f"{self.name}, стоимость: {self.price} Р"
    def return_price(self):
        return self.price

    def return_work(self):
        return f"{self.name}, стоимость: {self.price} Р"

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def get_absolute_url(self):
        return reverse('work:work_detail',
                       args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Work, self).save(*args, **kwargs)


