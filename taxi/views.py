from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation.trans_real import catalog

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    visits = request.session.get("visits", 0)
    request.session["visits"] = visits + 1
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "visits": request.session["visits"],
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(request, template_name="taxi/index.html", context=context)
