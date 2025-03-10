from django.urls import path
import taxi.views

urlpatterns = [
    path("", taxi.views.index, name="index")
]

app_name = "taxi"
