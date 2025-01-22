from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from taxi.models import Manufacturer, Car, Driver

def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count()
    }
    return render(
        request,
        "taxi/index.html",
        context=context
    )
