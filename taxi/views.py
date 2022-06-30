from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    context = {
        "number_of_drivers": Driver.objects.count(),
        "number_of_manufacturers": Manufacturer.objects.count(),
        "number_of_cars": Car.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)

