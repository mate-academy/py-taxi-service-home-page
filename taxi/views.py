from django.http import HttpRequest
from taxi.models import Driver, Manufacturer, Car
from django.template.loader import render_to_string
from django.http import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
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
