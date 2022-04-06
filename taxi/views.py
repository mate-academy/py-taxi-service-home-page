from django.shortcuts import render

from taxi.models import Car, Manufacturer, Driver


def index(request):
    count_cars = Car.objects.count()
    count_manufacturers = Manufacturer.objects.count()
    count_drivers = Driver.objects.count()

    context = {
        'count_cars': count_cars,
        'count_manufacturers': count_manufacturers,
        'count_drivers': count_drivers,

    }

    return render(request, 'taxi/index.html', context)
