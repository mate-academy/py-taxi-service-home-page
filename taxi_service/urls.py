from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from taxi_service import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxi.urls", namespace="taxi")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
