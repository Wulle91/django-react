# Generated by Django 3.2.19 on 2023-06-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_jbyuxy.jpg', upload_to='images/'),
        ),
    ]
