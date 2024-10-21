from django.http import HttpRequest, HttpResponse
from .models import Manufacturer, Driver, Car
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(request, "taxi/index.html", context=context)
