from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Manufacturer, Car


def index(request):
    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }
    return render(request, "taxi/index.html", context)
