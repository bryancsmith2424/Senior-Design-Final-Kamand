from django.urls import path

from . import views

urlpatterns = [

path('', views.index, name='scheduler'),
path('start', views.start, name='start'),
path('goals', views.goals, name='goals'),
path('update_goals', views.update_goals, name='update_goals'),
path('assignments', views.assignments, name='add_assignments'),
path('update_assignments', views.update_assignments, name='update_assignments'),
path('importcalander', views.get_calendar_data, name = 'importcalander'),
path('create_schedule', views.create_schedule, name = 'create_schedule'),
path('profile', views.profile, name = 'profile'),
path('edit/assignments', views.edit_assignments, name = 'edit_assignments'),
path('delete_assignments', views.delete_assignments, name = 'delete_assignments'),
path('edit/courses', views.edit_courses, name = 'edit_courses'),
path('delete_courses', views.delete_courses, name = 'delete_courses'),
path('logout', views.pagelogout, name= 'logout'),
path('assignments_number', views.assignments_number, name="assignments"),
]
#path('', views.index, name='scheduler'),
