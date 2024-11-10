from django.shortcuts import render
from .models import Driver, Manufacturer, Car

def index(request):
    num_drivers = Driver.objects.count()          # Підрахунок водіїв
    num_manufacturers = Manufacturer.objects.count()  # Підрахунок виробників
    num_cars = Car.objects.count()                # Підрахунок автомобілів

    context = {
        'num_drivers': num_drivers,
        'num_manufacturers': num_manufacturers,
        'num_cars': num_cars,
    }

    return render(request, 'taxi/index.html', context) #templates???