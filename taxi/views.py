from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from taxi.models import Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = get_user_model().objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)
