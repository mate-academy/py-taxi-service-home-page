from django.http import HttpRequest
from django.shortcuts import render
from .models import Driver, Car, Manufacturer

def index(request: HttpRequest):
    num_drivers = Driver.objects.count()
    num_manufacturer = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers" : num_drivers,
        "num_manufacturers" : num_manufacturer,
        "num_cars" : num_cars
    }
    return render(request=request, template_name='taxi/index.html', context=context)
