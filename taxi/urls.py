from django.urls import path
from taxi.views import index

app_name = "taxi"

urlpatterns = [  # 2
    path("", index, name="index"),
]
