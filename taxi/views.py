from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from taxi.models import Driver, Car, Manufacturer


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()

    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context)
