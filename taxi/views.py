from django.shortcuts import render
from taxi.models import Manufacturer, Driver, Car


def index(request):
    number_drivers = Driver.objects.count()
    number_manufacturers = Manufacturer.objects.count()
    number_cars = Car.objects.count()
    drivers_info = list(Driver.objects.all())

    context = {
        "num_drivers" : number_drivers,
        "num_manufacturers" : number_manufacturers,
        "num_cars" : number_cars,
        "drivers_info" : drivers_info
    }
    return render(request=request, template_name="taxi/index.html", context=context)

