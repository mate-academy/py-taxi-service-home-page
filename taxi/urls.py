from django.urls import path

from taxi.views import home_page

app_name = "taxi"
urlpatterns = [
    path("", home_page, name="index"),
]
