# Generated by Django 4.1.3 on 2023-02-14 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_comment_pub_date_alter_feedbacklist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='feedbacklist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='maincart',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
