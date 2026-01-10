from django.conf.urls.static import static
from django.urls import path

from taxi_service import settings
from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
] + static(settings.STATIC_URL)

app_name = "taxi"
