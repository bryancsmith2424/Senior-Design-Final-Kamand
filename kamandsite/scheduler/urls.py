from django.urls import path

from . import views

urlpatterns = [

path('', views.index, name='scheduler'),
path('<int:user_id>/start', views.start, name='start'),
path('<int:user_id>/goals', views.goals, name='goals'),
path('<int:user_id>/update_goals', views.update_goals, name='update_goals')
]
#path('', views.index, name='scheduler'),
