from django.urls import path
from . import views

urlpatterns = [
# Порожні лапки '' означають головну сторінку http://127.0.0.1:8000/
    path('', views.index, name='index'), #має вести до вьвс
]
