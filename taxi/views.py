from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(request, "taxi/index.html", context=context)


def car(request):
    car_query = Car.objects.all().values(
        "id",
        "model",
        "manufacturer__name"
    )
    context = {
        "car_query": car_query
    }
    return render(request, "taxi/car.html", context=context)


def driver(request):
    driver_query = Driver.objects.all().values(
        "id",
        "username",
        "first_name",
        "last_name"
    )
    context = {
        "driver_query": driver_query
    }
    return render(request, "taxi/driver.html", context=context)
