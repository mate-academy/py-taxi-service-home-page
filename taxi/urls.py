from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="home_page"),
]

app_name = "taxi"
