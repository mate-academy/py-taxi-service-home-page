from taxi.models import Car, Manufacturer, Driver

from django.shortcuts import render


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }

    return render(
        request=request,
        template_name="taxi/index.html",
        context=context,
    )
