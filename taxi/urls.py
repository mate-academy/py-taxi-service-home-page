from django.urls import path
from taxi import views  # importação absoluta

app_name = "taxi"

urlpatterns = [
    path('', views.index, name='index'),
]
