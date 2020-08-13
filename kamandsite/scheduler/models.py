from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from googleapiclient.discovery import build

from scheduler.modules.GreedyAlgo import greedyAlgo
from scheduler.modules.OptimalEvent import OptimalEvent
from scheduler.modules.Event import Event
from scheduler.modules.FindAvailableTime import findAvailableTime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class1 = models.CharField(max_length=50, blank=True)
    class2 = models.CharField(max_length=50, blank=True)
    class3 = models.CharField(max_length=50, blank=True)
    class4 = models.CharField(max_length=50, blank=True)
    class5 = models.CharField(max_length=50, blank=True)
    class6 = models.CharField(max_length=50, blank=True)
    class7 = models.CharField(max_length=50, blank=True)
    class8 = models.CharField(max_length=50, blank=True)

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=50, blank=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    Homework = 'HW'
    Project = 'Pr'
    Exam = 'Ex'
    Assignment_Type_Choices = [
        (Homework, 'Homework'),
        (Project, 'Project'),
        (Exam, 'Exam'),
    ]
    assignment_type = models.CharField(
        max_length=2,
        choices=Assignment_Type_Choices,
        default=Homework,
    )

    assignment_name = models.CharField(max_length=25, blank=True)
    deadline = models.DateTimeField()
    time_to_complete_estimate = models.DurationField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
            pass
'''
@receiver(post_save, sender=User)
def save_user_course(sender, instance, **kwargs):
    try:
        instance.course.save()
    except Profile.DoesNotExist or AttributeError:
            pass
'''
