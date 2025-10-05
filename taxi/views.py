from django.contrib.auth import get_user_model
from django.http import HttpResponse

from taxi.models import Manufacturer, Car
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }
    return render(request, "taxi/base.html", context=context)
