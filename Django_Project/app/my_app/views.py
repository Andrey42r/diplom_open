from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Trip


# Create your views here.
def menu(request):
    """
    Представление для отображения меню.
    """
    return render(request, 'menu.html')


def button(request):
    """
    Представление, которое перенаправляет на страницу меню.
    """
    return render(request, 'menu.html')


def index(request):
    """
    Представление для обработки данных о поездке и вычисления стоимости.
    Обрабатывает POST-запросы, сохраняет данные в базе данных и отображает результат.
    Если запрос GET, отображает форму для ввода данных.
    """
    if request.method == "POST":
        form = Trip.objects.all()
        distance = request.POST.get('distance')
        fuel_consumption = request.POST.get('fuel_consumption')
        fuel_price = request.POST.get('fuel_price')
        trip = Trip.objects.create(distance=distance, fuel_price=fuel_price, fuel_consumption=fuel_consumption)
        result = (float(distance) / 100) * float(fuel_consumption) * float(fuel_price)
        print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
        context = {
            'print_': print_,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
