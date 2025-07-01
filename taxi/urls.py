from django.urls import path
from taxi.views import index # noqa

urlpatterns = [
    path("", view=index, name="index") # noqa
]

app_name = "taxi"
