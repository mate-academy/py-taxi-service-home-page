from django.shortcuts import render
from .models import Driver, Manufacturer, Car


def index(request) -> HttpResponse:
    num_drivers: int = Driver.objects.count()
    num_manufacturers: int = Manufacturer.objects.count()
    num_cars: int = Car.objects.count()
    context: dict = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context)
