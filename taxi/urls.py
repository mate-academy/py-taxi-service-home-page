from django.urls import path
import taxi.views
from taxi.views import index

urlpatterns = [
    path("", taxi.views.index, name="index")
]


app_name = "taxi"
