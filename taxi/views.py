from typing import Any

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Manufacturer, Car


def index(request: HttpRequest) -> Any:
    num_drivers = get_user_model().objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(
        request=request,
        template_name="taxi/index.html",
        context=context,
    )
