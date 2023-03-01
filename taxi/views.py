from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car
def index(request):
    num_driver = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_driver,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(
        request,
        "taxi/index.html",
        context=context,
    )