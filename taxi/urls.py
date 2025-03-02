from django.urls import path
from taxi.views import index
app_name = "taxi"  # Це необхідно для `namespace`

urlpatterns = [
    path("", index, name="index"),  # Тут має бути хоча б один маршрут
]
