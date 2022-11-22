# blog/models.py
from django.db import models
from django.db.models import ImageField


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

