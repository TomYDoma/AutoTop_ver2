# Generated by Django 4.1.3 on 2022-11-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_feedbacklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacklist',
            name='email',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='feedbacklist',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='feedbacklist',
            name='number',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
