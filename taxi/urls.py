from django.urls import path
from taxi.views import index

urlpatterns = [  # 2
    path("", index, name="index"),
]
