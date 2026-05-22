from django.http import HttpResponse
from django.template.loader import render_to_string

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

    rendered_template = render_to_string(
        "taxi/index.html",
        context=context,
        request=request,
    )
    return HttpResponse(rendered_template)
