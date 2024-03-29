# Generated by Django 4.1.7 on 2023-03-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_categorywork_work"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "Категория автозапчастей",
                "verbose_name_plural": "Категории автозапчастей",
            },
        ),
        migrations.AlterModelOptions(
            name="categorywork",
            options={
                "ordering": ("name",),
                "verbose_name": "Категория работ",
                "verbose_name_plural": "Категории работ",
            },
        ),
        migrations.AddField(
            model_name="work",
            name="available",
            field=models.BooleanField(default=True),
        ),
    ]
