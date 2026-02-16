from django.urls import path

from taxi import views views

app_name = 'taxi'

urlpatterns = [
    path('', views.index, name='index'),  # головна сторінка
]
