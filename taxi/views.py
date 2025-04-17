from django.shortcuts import render
from .models import Driver, Manufacturer, Car

def index(request):
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    return render(request, 'taxi/index.html', {
        'num_drivers': num_drivers,
        'num_manufacturers': num_manufacturers,
        'num_cars': num_cars,
    })
