from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request) -> None:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
