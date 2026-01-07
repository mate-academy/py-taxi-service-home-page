from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car # Краще імпортувати моделі так

def index(request):
    # Рахуємо кількість об'єктів у базі
    num_drivers = Driver.objects.count() # Можна писати відразу .count() без .all()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    # Створюємо словник з даними для шаблону
    context = {
        'num_drivers': num_drivers,
        'num_manufacturers': num_manufacturers,
        'num_cars': num_cars,
    }

    return render(request, 'taxi/index.html', context=context)