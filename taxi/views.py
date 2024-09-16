from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    drivers_amount = Driver.objects.count()
    manufacturers_amount = Manufacturer.objects.count()
    cars_amount = Car.objects.count()
    context = {
        "drivers_amount": drivers_amount,
        "manufacturers_amount": manufacturers_amount,
        "cars_amount": cars_amount
    }
    return render(request, "taxi/index.html", context=context)
