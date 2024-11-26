from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request):
    content = {
        "num_cars": Car.objects.count(),
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context=content)
