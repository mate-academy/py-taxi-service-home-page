from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request):
    context = {
        "num_drivers" : Driver.objects.all().count(),
        "num_manufacturers" : Manufacturer.objects.all().count(),
        "num_cars" : Car.objects.all().count(),
    }

    return render(request, "taxi/index.html", context=context)
