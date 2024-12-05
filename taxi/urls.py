from django.urls import path
from . import views

app_name = 'taxi'

urlpatterns = [
    path('', views.index, name='index'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('cars/', views.cars, name='cars'),
    path('drivers/', views.drivers, name='drivers'),
]
