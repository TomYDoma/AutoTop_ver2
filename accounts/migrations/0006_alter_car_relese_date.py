# Generated by Django 4.1.3 on 2023-01-12 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Relese_Date',
            field=models.DateField(default=datetime.datetime(2023, 1, 12, 21, 19, 16, 933324), verbose_name='Дата выпуска'),
        ),
    ]