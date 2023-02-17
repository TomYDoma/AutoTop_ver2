# Generated by Django 4.1.3 on 2023-02-13 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_comment_pub_date_alter_feedbacklist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 19, 3, 5, 755527), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='feedbacklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 19, 3, 5, 754506)),
        ),
        migrations.AlterField(
            model_name='maincart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 19, 3, 5, 754506)),
        ),
    ]
