from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(requests):
    count_drivers = Driver.objects.count()
    count_manufacturers = Manufacturer.objects.count()
    count_cars = Car.objects.count()

    return render(requests, "taxi/index.html")
