from django.contrib import admin
from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
]
