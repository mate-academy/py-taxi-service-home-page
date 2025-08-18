


from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index

app_name = 'taxi'

urlpatterns = [
    path('', views.index, name='index')
    ]