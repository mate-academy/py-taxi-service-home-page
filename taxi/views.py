from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    all_cars = Car.objects.all()
    context = {"num_drivers": num_drivers,
               "num_manufacturers": num_manufacturers,
               "num_cars": num_cars}
    return render(request, "taxi/index.html", context=context)
