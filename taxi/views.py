from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from taxi.models import Manufacturer, Driver, Car


def index(request: HttpRequest) -> HttpResponse:
    request.session["visits"] = request.session.get("visits", 0) + 1
    num_drivers = Driver.objects.count()
    num_manufaxturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufaxturers,
        "num_cars": num_cars,
        "num_visits": request.session["visits"]
    }
    return render(request, "taxi/index.html", context=context)
