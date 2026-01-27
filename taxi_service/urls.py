from django.contrib import admin
from django.urls import path, include # Importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionar o caminho para as URLs da app taxi com namespace
    path("", include("taxi.urls", namespace="taxi")),
]
