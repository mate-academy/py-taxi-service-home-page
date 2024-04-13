from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Manufacturer, Driver, Car


def index(request: HttpRequest) -> HttpResponse:
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {"num_cars": num_cars,
               "num_drivers": num_drivers,
               "num_manufacturers": num_manufacturers}
    return render(request, template_name="taxi/index.html", context=context)
