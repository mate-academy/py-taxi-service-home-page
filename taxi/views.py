from django.shortcuts import render
from django.http import HttpRequest
from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> render:
    drives = Driver.objects.count()
    manufacturers = Manufacturer.objects.count()
    cars = Car.objects.count()
    print(drives)
    context = {
        "num_drivers": drives,
        "num_manufacturers": manufacturers,
        "num_cars": cars,
    }
    return render(request, "taxi/index.html", context=context)
