from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    number_of_drivers = Driver.objects.all().count()
    number_of_manufacturers = Manufacturer.objects.count()
    number_of_cars = Car.objects.count()

    context = {
        "number_of_drivers": number_of_drivers,
        "number_of_manufacturers": number_of_manufacturers,
        "number_of_cars": number_of_cars,
    }

    return render(request, "taxi/index.html", context=context)
