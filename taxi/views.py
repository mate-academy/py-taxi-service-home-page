from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from taxi.models import Car, Manufacturer, Driver
def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all().count()
    num_manufacturers =  Manufacturer.objects.all().count()
    num_cars =  Car.objects.all().count()
    return
