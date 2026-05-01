from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from taxi.views import index

app_name = "taxi"

urlpatterns = [
    path("", index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
