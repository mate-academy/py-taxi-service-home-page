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


def manufacturer(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        "manufacturers": manufacturers
    }
    return render(request, "taxi/manufacturer.html", context=context)


def car(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, "taxi/car.html", context=context)


def driver(request):
    drivers = Driver.objects.all()
    context = {
        "drivers": drivers
    }
    return render(request, "taxi/driver.html", context=context)
