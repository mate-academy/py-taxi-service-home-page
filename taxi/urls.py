from django.contrib import admin
from django.urls import path
from . import views
from .views import home_page

app_name = "taxi"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", home_page),
    path("admin/", admin.site.urls),
]
