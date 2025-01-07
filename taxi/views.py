from django.shortcuts import render
from .models import Driver, Manufacturer, Car
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    num_of_drivers = Driver.objects.all().count()
    num_of_manufacturers = Manufacturer.objects.all().count()
    num_of_cars = Car.objects.all().count()
    context = {
        "num_drivers": num_of_drivers,
        "num_manufacturers": num_of_manufacturers,
        "num_cars": num_of_cars,
    }
    return render(request=request,
                  template_name="taxi/index.html",
                  context=context)
