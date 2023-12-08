from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("taxi.urls", namespace="taxi")),  # 1
    path("admin/", admin.site.urls),
]
