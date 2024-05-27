from django.http import HttpResponse
from django.shortcuts import render

from .models import Driver, Manufacturer, Car

def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return HttpResponse("<h1>Hello world</h1>")
