from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car

def index(request):
    drivers = Driver.objects.all().count()
    manufacturers = Manufacturer.objects.all().count()
    cars = Car.objects.all().count()

    context = {
        "num_drivers": drivers,
        "num_manufacturers": manufacturers,
        "num_cars": cars,
    }

    return render(request, "taxi/index.html", context=context)