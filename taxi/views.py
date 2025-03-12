from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Car, Manufacturer

User = get_user_model()


def home_page(request: HttpRequest) -> render:
    num_cars = Car.objects.count()
    num_drivers = User.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,

    }
    return render(request, "taxi/index.html", context=context)
