# Generated by Django 4.1.7 on 2023-03-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0019_alter_car_relese_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="Relese_Date",
            field=models.CharField(max_length=50, verbose_name="Год выпуска"),
        ),
    ]
