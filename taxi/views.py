from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Driver, Manufacturer, Car


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<html><h1>Home page</h1><html>")


def index(request):
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)
