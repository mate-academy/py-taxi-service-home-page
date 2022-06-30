from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(requests):
    drivers = Driver.objects.count()
    manufacturer = Manufacturer.objects.count()
    cars = Car.objects.count()

    context = {
        "drivers": drivers,
        "manufacturer": manufacturer,
        "cars": cars
    }
    return render(requests, "taxi/index.html", context)



