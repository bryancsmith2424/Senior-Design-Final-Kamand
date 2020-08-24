from django.urls import path

from . import views

urlpatterns = [

path('', views.index, name='scheduler'),
path('start', views.start, name='start'),
path('goals', views.goals, name='goals'),
path('update_goals', views.update_goals, name='update_goals'),
path('assignments', views.assignments, name='assignments'),
path('update_assignments', views.update_assignments, name='update_assignments'),
path('googleapitest', views.get_calendar_data, name = 'googleapitest'),
path('create_schedule', views.create_schedule, name = 'create_schedule')
]
#path('', views.index, name='scheduler'),
