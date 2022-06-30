from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request):
    context = {
        "cars": Car.objects.count(),
        "drivers": Driver.objects.count(),
        "manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
