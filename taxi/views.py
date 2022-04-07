from django.http import HttpResponse
from django.shortcuts import render


from .models import Driver, Manufacturer, Car


def index(request):
    drivers_count = Driver.objects.count()
    car_count = Car.objects.count()
    manufacturer_count = Manufacturer.objects.count()
    return render(
        request=request,
        template_name='taxi/index.html',
        context={
            'drivers_count': drivers_count,
            'car_count': car_count,
            'manufacturer_count': manufacturer_count,
        },
    )
