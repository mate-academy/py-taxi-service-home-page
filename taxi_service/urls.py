from django.contrib import admin
from django.urls import path, include

import taxi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxi.urls", namespace="taxi"))
]
