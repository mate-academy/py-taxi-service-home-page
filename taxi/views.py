from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    total_drivers = Driver.objects.count()
    total_manufacturers = Manufacturer.objects.count()
    total_cars = Car.objects.count()

    context = {
        "total_drivers": total_drivers,
        "total_manufacturers": total_manufacturers,
        "total_cars": total_cars,
    }

    return render(request, "taxi/index.html", context=context)
