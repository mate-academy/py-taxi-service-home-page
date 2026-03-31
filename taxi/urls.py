from django.urls import path
from django.conf.urls.static import static
from taxi.views import index
from django.conf import settings

urlpatterns = [
    path("", index, name="index")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name = "taxi"
