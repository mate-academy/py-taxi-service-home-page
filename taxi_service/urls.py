"""
taxi_service URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include(("taxi.urls", "taxi"), namespace="taxi")),
    path("admin/", admin.site.urls),
]
