from django.urls import path
from .views import index

print(">>> ŁADUJĘ taxi/urls.py")
urlpatterns = [
    path("", index, name="index"),
]
app_name = "taxi"