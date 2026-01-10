from django.shortcuts import render

from .models import Driver, Manufacturer, Car


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
