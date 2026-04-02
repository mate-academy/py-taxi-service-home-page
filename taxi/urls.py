from django.urls import path
from django.conf import settings

from taxi.views import index


less_words = settings.STATIC_ROOT
urlpatterns = ([path("",
                     index,
                     name="index")
                ])

app_name = "taxi"
