from operator import index

from django.urls import path
from . import views

app_name = 'taxi'
urlpatterns = [
    path('', views.index, name='index'),
]