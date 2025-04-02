from django.urls import path
from . import views

app_name = 'taxi'  # This sets the application namespace

urlpatterns = [
    path('', views.index, name='index'),
]
