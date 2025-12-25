from django.shortcuts import render
from .models import Driver, Car, Manufacturer
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    return render(request,
                  "taxi/index.html",
                  context={"num_drivers": num_drivers,
                           "num_manufacturers": num_manufacturers,
                           "num_cars": num_cars})
