# Generated by Django 4.1.7 on 2023-03-16 11:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0006_orderautopart_rename_end_date_order_end_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="start_date",
            new_name="created",
        ),
    ]
