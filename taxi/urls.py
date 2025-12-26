from django.conf.urls.static import static
from django.urls import path

from taxi.views import index
from taxi_service import settings


urlpatterns = [
    path("", index, name="index"),
] + static(settings.STATIC_URL)

app_name = "taxi"
