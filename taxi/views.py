from django.shortcuts import render
from django.http import HttpResponse
from taxi.models import Driver, Manufacturer, Car


def hi(request):
    return HttpResponse(
        "<html>"
        "<h1>HI</h1>"
        "</html>"
    )


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }

    return render(request, "taxi/index.html", context=context)
