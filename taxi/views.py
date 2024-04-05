from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from .models import Driver
from .models import Manufacturer
from .models import Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    contex = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", contex)


