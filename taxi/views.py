from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import (
    Car,
    Driver,
    Manufacturer,
)
from .services.get_count import get_objects_count


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": get_objects_count(Driver),
        "num_manufacturers": get_objects_count(Manufacturer),
        "num_cars": get_objects_count(Car),
    }
    return render(request, "taxi/index.html", context)
