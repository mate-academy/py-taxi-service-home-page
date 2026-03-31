from django.shortcuts import render
from taxi.models import Manufacturer, Car, Driver


def index(request):
    drivers_num = Driver.objects.count()
    car_num = Car.objects.count()
    manufacturer_num = Manufacturer.objects.count()
    context = {
        "drivers_num": drivers_num,
        "car_num": car_num,
        "manufacturer_num": manufacturer_num
    }
    return render(request, "taxi/index.html", context=context)
