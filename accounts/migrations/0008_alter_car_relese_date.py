# Generated by Django 4.1.3 on 2023-02-13 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_car_relese_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Relese_Date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 18, 2, 18, 203266), verbose_name='Дата выпуска'),
        ),
    ]