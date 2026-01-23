from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


from .views import index, manufacturer, car, driver


app_name = 'taxi'


urlpatterns = [
    path('', views.index, name='index'),
    path('manufacturers/', views.manufacturer, name='manufacturers'),
    path('cars/', views.car, name='cars'),
    path('drivers/', views.driver, name='drivers'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
