from django.urls import path, include
from taxi import views

app_name = "taxi"

urlpatterns = [path("", views.index, name="index")]
