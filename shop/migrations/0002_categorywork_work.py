# Generated by Django 4.1.7 on 2023-03-20 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryWork",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=200)),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Название работы"),
                ),
                ("image", models.ImageField(blank=True, upload_to="work/%Y/%m/%d")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Стоимость"
                    ),
                ),
                ("execution_Time", models.IntegerField(verbose_name="Срок выполнения")),
                ("warranty", models.IntegerField(verbose_name="Гарантия")),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="work",
                        to="shop.categorywork",
                    ),
                ),
            ],
            options={
                "verbose_name": "Работа",
                "verbose_name_plural": "Работы",
                "ordering": ("name",),
                "index_together": {("id", "slug")},
            },
        ),
    ]
