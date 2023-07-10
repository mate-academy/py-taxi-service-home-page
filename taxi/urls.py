from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="index")
]


app_name = "taxi"








# from django.urls import path
#
# from catalog.views import index, hello_world
#
# # name указывать
# urlpatterns = [
#     path("", index, name="index"),
#     path("hello-world/<int:unique_number>/", hello_world, name="hello-world"),
# ]
#
# # для namespace в urls
# app_name = "catalog"