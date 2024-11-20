from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    data_to_template = {
        'num_drivers': num_drivers,
        'num_manufacturers': num_manufacturers,
        'num_cars': num_cars,
    }

    return render(request, 'taxi/index.html', data_to_template)  # виводимо шаблон
