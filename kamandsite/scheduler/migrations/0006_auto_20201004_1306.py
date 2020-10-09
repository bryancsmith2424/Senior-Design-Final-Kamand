# Generated by Django 3.0.5 on 2020-10-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_assignment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='class1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class4',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class5',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class6',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class7',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='class8',
        ),
        migrations.AddField(
            model_name='profile',
            name='day_end_offset',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='day_start_offset',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='productive_time',
            field=models.CharField(choices=[('EB', 'Homework'), ('MM', 'Project'), ('MD', 'Exam'), ('AA', 'Homework'), ('EE', 'Project'), ('NN', 'Exam')], default='AA', max_length=2),
        ),
    ]
