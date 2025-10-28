from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer

# Create your views here.

def index(request):
  context = {
    "num_drivers": Driver.objects.all().count(),
    "num_manufacturers": Manufacturer.objects.all().count(),
    "num_cars": Car.objects.all().count()
  }

  return render(request, 'taxi/index.html', context=context)
