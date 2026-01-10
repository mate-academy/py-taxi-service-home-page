from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(requests):
    count_drivers = Driver.objects.count()
    count_manufacturers = Manufacturer.objects.count()
    count_cars = Car.objects.count()

    context = {
        "count_drivers": count_drivers,
        "count_manufacturers": count_manufacturers,
        "count_cars": count_cars
    }

    return render(requests, "taxi/index.html",context=context)
