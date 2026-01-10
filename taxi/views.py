from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Manufacturer, Car


def index(request) -> HttpResponse:
    num_drivers = get_user_model().objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    return render(
        request,
        "taxi/index.html",
        {
            "num_drivers" : num_drivers,
            "num_manufacturers" : num_manufacturers,
            "num_cars" : num_cars
        }
    )
