from django.http import HttpResponse
from django.shortcuts import render
from .models import Driver, Manufacturer, Car


def index(request):
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)


def manufacturers_list(request):
    return HttpResponse("Заглушка для списка производителей")


def cars_list(request):
    return HttpResponse("Заглушка для списка автомобилей")


def drivers_list(request):
    return HttpResponse("Заглушка для списка водителей")
