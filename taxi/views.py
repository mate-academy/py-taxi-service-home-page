from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": Driver.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
            "num_cars": Car.objects.count(),
        }
    )
