from django.urls.conf import path, include
from taxi import views
urlpatterns = [
    path("", views.index, name="index")
]

app_name = "taxi"
