from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "taxi"
