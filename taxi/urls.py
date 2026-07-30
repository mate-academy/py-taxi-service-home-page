
from django.urls import path, include
from taxi.views import index
urlpatterns = [
    # Викликаємо функцію index для головної сторінки
    path("", index, name="index"),
]

app_name = "taxi"
