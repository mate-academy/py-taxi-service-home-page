from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = get_user_model().objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    print(num_drivers, num_cars, num_manufacturers)
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(
        request,
        "taxi/index.html",
        context=context,
    )
