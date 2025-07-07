from django.shortcuts import render
from .models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context)


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        "manufacturers": manufacturers,
    }
    return render(request, "taxi/manufacturer_list.html", context)


def car_list(request):
    cars = Car.objects.all()
    context = {
        "cars": cars,
    }
    return render(request, "taxi/car_list.html", context)


def driver_list(request):
    drivers = Driver.objects.all()
    context = {
        "drivers": drivers,
    }
    return render(request, "taxi/driver_list.html", context)