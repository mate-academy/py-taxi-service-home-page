from django.urls import path
from taxi.views import *

urlpatterns = [  # 2
    path("", index, name="index"),
]
