# Generated by Django 4.1.3 on 2022-11-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]