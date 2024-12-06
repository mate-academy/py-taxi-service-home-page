from django.urls import path
from taxi import views
#from taxi_service.urls import urlpatterns


app_name = "taxi"
urlpatterns = [
    path("", views.index, name="index"),

]
