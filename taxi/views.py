from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {"num_drivers": num_drivers,
               "num_manufacturers": num_manufacturers,
               "num_cars": num_cars}
    rendered = render_to_string("taxi/index.html", context)
    return HttpResponse(rendered)
