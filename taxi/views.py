from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_drivers = Driver.objects.count()
    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers
    }
    return render(request, template_name="taxi/index.html", context=context)
