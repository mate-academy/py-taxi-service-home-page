from django.shortcuts import render
from taxi.models import Manufacturer, Driver, Car


def index(request):
    number_drivers = Driver.objects.count()
    number_manufacturers = Manufacturer.objects.count()
    number_cars = Car.objects.count()

    context = {
        "num_drivers" : number_drivers,
        "num_manufacturers" : number_manufacturers,
        "num_cars" : number_cars
    }
    return render(request=request, template_name="base.html", context=context)


def drivers(request):
    drivers = list(Driver.objects.values_list("first_name",
                                              "last_name",
                                              "license_number"))
    name_drivers = ";   ".join([" ".join(driver) for driver in drivers])
    context = {
        "name_drivers" : name_drivers
    }
    return render(request, template_name="taxi/drivers.html", context=context)
