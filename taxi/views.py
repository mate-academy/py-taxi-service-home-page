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
        "num_cars": num_cars
    }
    return render(request,
                  "taxi/index.html",
                  context=context
                  )


def cars(request: HttpRequest) -> HttpResponse:
    cars_all = Car.objects.all()
    models = [car.model for car in cars_all]

    context = {
        "models": models
    }
    return render(request,
                  "taxi/cars.html",
                  context=context
                  )


def drivers(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    context = {
        "num_drivers": num_drivers
    }
    return render(request,
                  "taxi/drivers.html",
                  context=context
                  )


def manufacturers(request: HttpRequest) -> HttpResponse:
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_manufacturers": num_manufacturers
    }
    return render(request,
                  "taxi/manufacturers.html",
                  context=context
                  )
