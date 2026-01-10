from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context=context)


def drivers(request: HttpRequest) -> HttpResponse:
    context = {
        "drivers": Driver.objects.all()
    }

    return render(request, "taxi/drivers.html", context=context)


def cars(request: HttpRequest) -> HttpResponse:
    context = {
        "cars": Car.objects.all()
    }

    return render(request, "taxi/cars.html", context=context)


def manufacturers(request: HttpRequest) -> HttpResponse:
    context = {
        "manufacturers": Manufacturer.objects.all()
    }

    return render(
        request,
        "taxi/manufacturers.html",
        context=context,
    )
