# Generated by Django 2.2.12 on 2022-07-20 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20220720_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='profile',
        ),
    ]