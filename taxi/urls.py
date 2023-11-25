from django.urls import path
from taxi.views import index
from django.contrib import admin

urlpatterns = [
    path("admin", admin.site.urls),
    path("taxi/", index)
]

app_name = "taxi"
