from django.urls import path
from taxi.views import index # noqa


app_name = "taxi"

urlpatterns = [
    path("", view=index, name="index") # noqa
]
