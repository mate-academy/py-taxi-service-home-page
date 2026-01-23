from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


from .views import index, manufacturer, car, driver

urlpatterns = [
    path('', views.index, name='index'),
    path('manufacturers/', manufacturer, name='manufacturers'),
    path('cars/', car, name='cars'),
    path('drivers/', driver, name='drivers'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = 'taxi'
