from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

from googleapiclient.discovery import build

from scheduler.modules.GreedyAlgo import greedyAlgo
from scheduler.modules.OptimalEvent import OptimalEvent
from scheduler.modules.Event import Event
from scheduler.modules.FindAvailableTime import findAvailableTime
