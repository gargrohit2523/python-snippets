""" Defines url patterns for learning log app"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #HomePage
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics')
]