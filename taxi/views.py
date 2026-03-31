from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from taxi.models import Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
