from django.contrib.auth import get_user_model

from django.shortcuts import render

from taxi.models import Manufacturer, Car


def index(request):
    num_drivers = get_user_model().objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
