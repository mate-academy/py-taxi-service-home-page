from django.shortcuts import render
from django.db.models import Count

from .models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.aggregate(count=Count("id"))["count"]
    num_manufacturers = Manufacturer.objects.aggregate(
        count=Count("id")
    )["count"]
    num_cars = Car.objects.aggregate(count=Count("id"))["count"]

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(request, "taxi/index.html", context)
