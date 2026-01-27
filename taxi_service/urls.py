from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # CORREÇÃO E261:
    path("taxi/", include("taxi.urls", namespace="taxi")),
]
