from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
