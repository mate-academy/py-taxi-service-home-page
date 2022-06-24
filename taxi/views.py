from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    context = {
        "title": "Taxi service",
        "drivers_amount": Driver.objects.count(),
        "manufacturers_amount": Manufacturer.objects.count(),
        "cars_amount": Car.objects.count()
    }

    return render(request, "taxi/index.html", context=context)
