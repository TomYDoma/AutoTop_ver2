# Generated by Django 4.1.7 on 2023-04-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0024_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(default="default.png", upload_to="profile_images/"),
        ),
    ]
