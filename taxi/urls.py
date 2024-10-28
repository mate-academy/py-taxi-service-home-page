from django.urls import path
from taxi.views import index


# les liens pour l'applicaiton
urlpatterns = [
    path("", index, name="index")  # Home page URL
]

app_name = "taxi"
