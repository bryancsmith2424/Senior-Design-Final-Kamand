# Generated by Django 3.0.5 on 2020-10-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20201008_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timezone_offset',
            field=models.IntegerField(default=-4),
        ),
    ]