from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all().count()
    num_cars = Car.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
