from django.shortcuts import render
from django.http import HttpResponse
from taxi.models import Driver, Manufacturer, Car


def index(request):
    drivers_count = Driver.objects.count()
    manufacturers_count = Manufacturer.objects.count()
    cars_count = Car.objects.count()

    context = {
        "drivers_count": drivers_count,
        "manufacturers_count": manufacturers_count,
        "cars_count": cars_count
    }

    return render(request, "taxi/index.html", context=context)
