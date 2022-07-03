from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    amount_of_drivers = Driver.objects.count()
    amount_of_manufactures = Manufacturer.objects.count()
    amount_of_cars = Car.objects.count()
    context = {"amount_of_drivers": amount_of_drivers, "amount_of_manufactures": amount_of_manufactures,
               "amount_of_cars": amount_of_cars}

    return render(request, "taxi/index.html", context=context)
