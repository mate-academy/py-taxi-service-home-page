from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufactures = Manufacturer.objects.count()
    num_car = Car.objects.count()

    context = {
        "number_of_drivers": num_drivers,
        "number_of_manufacturers": num_manufactures,
        "number_of_cars": num_car,
    }

    return render(request, "taxi/index.html", context=context)
