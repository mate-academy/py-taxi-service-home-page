from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request):
    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": Driver.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
            "num_cars": Car.objects.count()
        }
    )
