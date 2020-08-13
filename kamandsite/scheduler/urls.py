from django.urls import path

from . import views

urlpatterns = [

path('', views.index, name='scheduler'),
path('start', views.start, name='start'),
path('goals', views.goals, name='goals'),
path('update_goals', views.update_goals, name='update_goals'),
path('assignments', views.assignments, name='assignments'),
path('update_assignments', views.update_assignments, name='update_assignments')
]
#path('', views.index, name='scheduler'),
