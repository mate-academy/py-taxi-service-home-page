from django.shortcuts import render


from taxi.models import Driver, Car, Manufacturer


def index(request):
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    return render(
        request,
        "taxi/index.html",
        {
            "num_drivers": num_drivers,
            "num_cars": num_cars,
            "num_manufacturers": num_manufacturers,
        },
    )
