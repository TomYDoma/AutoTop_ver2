# Generated by Django 4.1.3 on 2023-02-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_compositionorder_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compositionorder',
            name='ID_TypesWorks',
        ),
        migrations.AddField(
            model_name='compositionorder',
            name='ID_TypesWorks',
            field=models.ManyToManyField(to='order.typeswork'),
        ),
    ]