from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from .models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    contex = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers
    }
    return render(
        request=request,
        template_name="taxi/index.html",
        context=contex
    )
