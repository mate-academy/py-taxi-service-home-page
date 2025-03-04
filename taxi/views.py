from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
context = {
        "num_drivers" : Driver.objects.all().count(),
        "num_manufacturers" : Manufacturer.objects.all().count(),
        "num_cars" : Car.objects.all().count(),
    }
def index(request):
    return render(request, "taxi/index.html", context=context)

def cars(request):
    return render(request, "taxi/cars_list.html", context=context)

def drivers(request):
    return render(request, "taxi/drivers_list.html", context=context)

def manufacturers(request):
    return render(request, "taxi/manufacturers_list.html", context=context)
