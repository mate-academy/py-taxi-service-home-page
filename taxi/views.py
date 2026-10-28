from django.shortcuts import render
from django.http import HttpResponse
from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return HttpResponse(render(request, "taxi/index.html", {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }))
