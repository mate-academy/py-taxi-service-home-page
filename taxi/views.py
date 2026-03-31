from django.shortcuts import render
from .models import Car, Driver, Manufacturer
# Create your views here.


def index(request: dict):
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
