# Generated by Django 4.1.3 on 2022-11-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
