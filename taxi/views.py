from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    drivers_num = Driver.objects.count()
    manufacturers_num = Manufacturer.objects.count()
    cars_num = Car.objects.count()

    context = {
        "drivers_num": drivers_num,
        "manufacturers_num": manufacturers_num,
        "cars_num": cars_num
    }

    return render(request, "templates/taxi/index.html", context=context)
