from .models import Driver, Manufacturer, Car
from django.shortcuts import render


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return render(request, "taxi/index.html", {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    })


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, "taxi/manufacturer_list.html",
                  {"manufacturers": manufacturers})


def car_list(request):
    cars = Car.objects.all()
    return render(request, "taxi/car_list.html", {"cars": cars})


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, "taxi/driver_list.html", {"drivers": drivers})
