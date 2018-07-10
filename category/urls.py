from django.urls import path
from category import views

urlpatterns = [
    path('(?P<category>\w+)$', views.index),
]