from django.contrib import admin
from django.urls import path, include

from taxi.views import index

urlpatterns = [
    path("", include("taxi.urls", namespace="taxi")),  # 1
    path("admin/", admin.site.urls),
]
