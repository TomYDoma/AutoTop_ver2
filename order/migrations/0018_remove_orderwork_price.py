# Generated by Django 4.1.7 on 2023-03-20 14:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0017_alter_order_options_remove_order_autopart_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderwork",
            name="price",
        ),
    ]
