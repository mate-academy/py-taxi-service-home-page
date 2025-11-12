from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Manufacturer, Car


def index(request: HttpRequest):
    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }
    return render(
        request,
        "taxi/index.html",
        context=context
    )
