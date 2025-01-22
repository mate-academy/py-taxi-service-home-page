from django.contrib import admin
from django.urls import path
# Message for buddie: here is taxi/urls
from .views import index
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index")
]

app_name = "taxi"
