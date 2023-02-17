# Generated by Django 4.1.3 on 2023-02-13 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_comment_pub_date_alter_feedbacklist_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 18, 52, 12, 881106), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='feedbacklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 18, 52, 12, 880120)),
        ),
        migrations.AlterField(
            model_name='maincart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 13, 18, 52, 12, 880120)),
        ),
    ]
