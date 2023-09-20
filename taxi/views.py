from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest):
    return render(
        request,
        template_name="taxi/index.html",
        context={
            "num_drivers": Driver.objects.count(),
            "num_cars": Car.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
        },
        content_type="text/html",
    )
