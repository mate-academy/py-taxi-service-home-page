from django.http import HttpResponse, HttpRequest
from .models import Driver, Manufacturer, Car
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count()
    }

    return render(request, "taxi/index.html", context)
