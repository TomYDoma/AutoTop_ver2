# Generated by Django 4.1.3 on 2022-11-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_post_specialistadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialistadmin',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='specialistadmin',
            name='positions',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
