# Generated by Django 3.0.5 on 2020-07-14 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_assignment_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='coursename',
        ),
    ]
