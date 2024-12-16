from taxi import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
]

app_name = "taxi"
