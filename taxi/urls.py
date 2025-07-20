from django.urls import path

import taxi
from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "taxi"
