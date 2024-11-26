from django.urls import path

from taxi import views
from taxi.views import index

urlpatterns = [
    path("", views.index, name="index"),

]

app_name = "taxi"
