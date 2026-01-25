from django.urls import path
from taxi.views import index

app_name = "taxi"  # Простір імен додатка
urlpatterns = [
    path("", index, name="index"),
]
