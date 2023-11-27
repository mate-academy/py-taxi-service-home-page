from django.urls import path
from taxi.views import index
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
]

app_name = "taxi"
