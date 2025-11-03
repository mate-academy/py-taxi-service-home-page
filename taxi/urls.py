from django.urls import path
from . import views

app_name = "taxi"  # namespace do app

urlpatterns = [
    path('', views.index, name='index'),  # página inicial
]
