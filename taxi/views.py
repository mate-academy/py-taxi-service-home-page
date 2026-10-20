from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count()
    }

    return render(request, template_name="taxi/index.html", context=context)
