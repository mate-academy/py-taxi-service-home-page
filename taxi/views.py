from django.http import HttpRequest, HttpResponse

from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_of_drivers": Driver.objects.count(),
        "num_of_manufacturer": Manufacturer.objects.count(),
        "num_of_cars": Car.objects.count()
    }
    return render(request, "taxi/index.html", context)
