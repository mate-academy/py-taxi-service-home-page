from django.urls import path
from . import views

app_name = 'taxi'

urlpatterns = [
    path('', views.index, name='home'),
    path('manufacturers/', views.manufacturers_list, name='manufacturers-list'),
    path('cars/', views.cars_list, name='cars-list'),
    path('drivers/', views.drivers_list, name='drivers-list'),
]
