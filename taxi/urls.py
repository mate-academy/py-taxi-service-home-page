from django.urls import path

from taxi import views

urlpatterns = [
    path("", views.index, name="index")
]

app_name = "taxi"
