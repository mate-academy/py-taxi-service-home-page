from django.urls import path
from . import views

urlpatterns = [
    # O caminho "" corresponde à raiz do site quando incluído no urls principal
    path("", views.index, name="index"),
]
