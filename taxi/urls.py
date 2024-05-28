from django.urls import path

from taxi import views

urlpatterns = [
    path("index/", views.index, name="index")
]

app_name = "taxi"
