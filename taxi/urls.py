from django.urls import path, include

import taxi.views

urlpatterns = [
    path("", taxi.views.index, name="index")
]

app_name = "taxi"
