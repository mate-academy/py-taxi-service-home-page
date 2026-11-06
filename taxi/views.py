from django.http import HttpResponse
from django.template import loader

from taxi.models import Car, Driver, Manufacturer


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return HttpResponse(
        loader.render_to_string("taxi/index.html", context, request)
    )
