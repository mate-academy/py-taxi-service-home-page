from django.http import HttpRequest, HttpResponse
from django.template import loader

from taxi.models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    template = loader.get_template("taxi/index.html")
    return HttpResponse(template.render(context, request))
