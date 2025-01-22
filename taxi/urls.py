from django.urls import path
app_name = 'taxi'
from taxi.views import index
urlpatterns = [
    path('', index, name='index'),
]