from django.shortcuts import render

from taxi.models import Manufacturer, Driver, Car


def index(request):
    manufacturer_count = Manufacturer.objects.count()
    drivers_count = Driver.objects.count()
    cars_count = Car.objects.count()
    context = {
        "manufacturer_count": manufacturer_count,
        "drivers_count": drivers_count,
        "cars_count": cars_count
    }
    return render(request, 'taxi/index.html', context=context)
