from django.contrib import admin
from django.urls import path, include  # ✅ добавили include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("taxi.urls", "taxi"), namespace="taxi")),  # ✅ добавили маршрут для taxi
]