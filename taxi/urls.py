from django.urls import path
from django.conf.urls.static import static

from taxi.views import index

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
]
