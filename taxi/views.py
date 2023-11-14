from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(request, "taxi/index.html", context=context)




# в 4 перевірити: Don't forget to do all necessary steps so that Django can serve these static files.
# в 5 куда то додавати: Edit settings so that engine knows where to look for template source files.
# 6  Load static and import styles.css
#
#
#
#




