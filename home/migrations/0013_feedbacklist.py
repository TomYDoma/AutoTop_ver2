# Generated by Django 4.1.3 on 2022-11-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
