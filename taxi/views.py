from django.http import HttpResponse
from django.shortcuts import render
from taxi.models import Manufacturer, Driver, Car


def index(request):
    manufacturer_count = Manufacturer.objects.count()
    car_count = Car.objects.count()
    driver_count = Driver.objects.count()
    context = {
        "manufacturer_count": manufacturer_count,
        "car_count": car_count,
        "driver_count": driver_count
            }
    return render(request, "taxi/index.html", context=context)
