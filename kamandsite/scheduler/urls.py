from django.urls import path

from . import views

urlpatterns = [

path('', views.index, name='scheduler'),
path('start', views.start, name='start')
]
#path('', views.index, name='scheduler'),
