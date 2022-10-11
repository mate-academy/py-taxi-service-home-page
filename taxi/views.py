from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    cars = Car.objects.count()
    drivers = Driver.objects.count()
    manufacturers = Manufacturer.objects.count()

    context = {
        "cars": cars,
        "drivers": drivers,
        "manufacturers": manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
