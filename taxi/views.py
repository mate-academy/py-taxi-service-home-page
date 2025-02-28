from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, template_name="taxi/index.html", context=context)
