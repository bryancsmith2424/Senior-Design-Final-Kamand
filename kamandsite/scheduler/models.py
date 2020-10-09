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
    Early_Bird = 'EB'
    Morning_Magpie = 'MM'
    Mid_Day_Macaw = 'MD'
    Afternoon_Albatross = 'AA'
    Evening_Eagle = 'EE'
    Nocturnal_Nightingale = 'NN'
    Night_Owl = 'NO'
    Productive_Time_Choices = [
        (Early_Bird, 'Early Bird: 5am - 8am'),
        (Morning_Magpie, 'Morning_Magpie: 8am - 11am'),
        (Mid_Day_Macaw, 'Mid_Day_Macaw: 11am - 2pm'),
        (Afternoon_Albatross, 'Afternoon_Albatross: 2pm - 5pm'),
        (Evening_Eagle, 'Evening_Eagle: 5pm - 8pm'),
        (Night_Owl, 'Night Owl: 8pm - 10pm'),
        (Nocturnal_Nightingale, 'Nocturnal_Nightingale: 11pm - 2am'),
    ]
    productive_time = models.CharField(
        max_length=2,
        choices=Productive_Time_Choices,
        default=Afternoon_Albatross,
    )
    day_start_offset = models.IntegerField(default=0)
    day_end_offset = models.IntegerField(default=0)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursename = models.CharField(max_length=50, blank=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    Homework = 'HW'
    Quiz = 'QZ'
    Exam = 'EX'
    Assignment_Type_Choices = [
        (Homework, 'Homework'),
        (Quiz, 'Quiz'),
        (Exam, 'Exam'),
    ]
    assignment_type = models.CharField(
        max_length=2,
        choices=Assignment_Type_Choices,
        default=Homework,
    )

    assignment_name = models.CharField(max_length=25, blank=True)
    deadline = models.DateTimeField()
    #time_to_complete_estimate is in hours
    time_to_complete_estimate = models.FloatField(default = 1.0)


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
