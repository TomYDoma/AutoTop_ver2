# Generated by Django 4.1.3 on 2023-02-13 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_compositionworks_status_alter_car_relese_date_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compositionworks',
            options={'verbose_name': 'Состав заказов по работам', 'verbose_name_plural': 'Составы заказов по работам'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='car',
            name='Relese_Date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 19, 0, 30, 547864), verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Start_Date',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 19, 0, 30, 548867), verbose_name='Дата начала'),
        ),
    ]
