from django.contrib import admin

# Register your models here.
from .models import Profile, Course, Assignment, Scheduled_event
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Scheduled_event)
