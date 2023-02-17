# Generated by Django 4.1.3 on 2023-02-17 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_car_relese_date_alter_car_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Car',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='CompositionWorks',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Status',
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='defaultCar.jpg', upload_to='images'),
        ),
        migrations.DeleteModel(
            name='CompositionWorks',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
