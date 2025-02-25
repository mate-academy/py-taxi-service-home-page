from django.urls import path

from taxi.views import index

app_name = 'taxi'  # Set namespace

urlpatterns = [
    path("", index, name='index'),  # Home page route
]
