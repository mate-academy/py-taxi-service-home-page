from django.urls import path

from taxi import views

app_name = 'taxi'

urlpatterns = [
    path("", views.index, name="index")

]