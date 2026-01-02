# taxi_service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add this line to include your app's URLs
    path("", include("taxi.urls", namespace="taxi")),
]
