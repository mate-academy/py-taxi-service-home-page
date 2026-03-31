from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request):
    count_drivers = Driver.objects.all().count()
    count_manufacturer = Manufacturer.objects.all().count()
    count_cars = Car.objects.all().count()

    context = {
        "num_drivers": count_drivers,
        "num_manufacturers": count_manufacturer,
        "num_cars": count_cars,
    }
    return render(request, "taxi/index.html", context=context)
