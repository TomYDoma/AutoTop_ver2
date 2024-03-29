# Generated by Django 4.1.3 on 2023-01-12 21:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0023_alter_feedbacklist_date_alter_maincart_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 21, 5, 51, 904483), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='feedbacklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 21, 5, 51, 904483)),
        ),
        migrations.AlterField(
            model_name='maincart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 21, 5, 51, 903490)),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_Brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('Car_Model', models.CharField(max_length=50, verbose_name='Модель')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('PTS', models.CharField(max_length=50, verbose_name='ПТС')),
                ('State_Number', models.CharField(max_length=10, verbose_name='Номер')),
                ('VIN', models.CharField(max_length=17, verbose_name='VIN')),
                ('Color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('Relese_Date', models.DateField(default=datetime.datetime(2023, 1, 12, 21, 5, 51, 904483), verbose_name='Дата выпуска')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
