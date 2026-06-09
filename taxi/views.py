from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Driver, Manufacturer, Car


def index(request) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    html = render_to_string("taxi/index.html", context)
    return HttpResponse(html)
