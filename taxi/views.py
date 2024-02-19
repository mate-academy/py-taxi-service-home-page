from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    if not request.session.get("visits"):
        request.session["visits"] = 1
    else:
        request.session["visits"] += 1

    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
        "visits": request.session["visits"],
    }

    return render(request, "taxi/index.html", context)
