# Дипломный проект: Калькулятор стоимости поездки (Django)

Этот проект представляет собой веб-приложение на базе Django для расчета стоимости поездки, используя базу данных SQLite.

## Функциональность:

- **Расчет стоимости:** Пользователь вводит расстояние, расход топлива и цену топлива. Приложение рассчитывает и отображает общую стоимость поездки.
- **Сохранение истории поездок:**  История рассчитанных поездок сохраняется в локальной базе данных SQLite.
- **Удобный интерфейс:**  Используется простой и интуитивно понятный веб-интерфейс, созданный с помощью шаблонов Django.


## Технологии:

- **Django:** Веб-фреймворк Python.
- **Python:** Язык программирования.
- **SQLite:** Система управления базами данных (СУБД).
- **HTML, CSS, JavaScript (вероятно):** Для создания веб-интерфейса. (Требуется подтверждение в коде)


## Установка и запуск:

**Предварительные требования:**

- Python 3.x
- Django

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/Andrey42r/diplom_open.git
   cd diplom_open/Django_Project/app
2. **Создание виртуального окружения (рекомендуется):**

       python3 -m venv .venv
       source .venv/bin/activate  # Linux/macOS
       .venv\Scripts\activate  # Windows

3. **Запуск сервера разработки Django:**

         python manage.py runserver

Приложение будет запущено на http://127.0.0.1:8000/.

Структура проекта:

    models.py: Определяет модели Django для работы с базой данных SQLite.
    forms.py:  Определяет формы для ввода данных пользователем.
    views.py: Содержит обработчики представлений Django.
    urls.py: Определяет маршруты URL.
    templates/: Директория с шаблонами HTML.

Примеры кода (фрагменты):

1. Модель Trip (models.py):

        from django.db import models

        class Trip(models.Model):
            distance = models.FloatField(default=0, null=True)
            fuel_consumption = models.FloatField(default=0, null=True)
            fuel_price = models.FloatField(default=0, null=True)  

2. Обработчик формы (views.py):

         from django.http import HttpResponse, HttpResponseRedirect
         from django.shortcuts import render, redirect
         from .models import Trip

         def menu(request):
             return render(request, 'menu.html')

         def button(request):
             return render(request, 'menu.html')

         def index(request):
             if request.method == "POST":
                form = Trip.objects.all()
                distance = request.POST.get('distance')
                fuel_consumption = request.POST.get('fuel_consumption')
                fuel_price = request.POST.get('fuel_price')
                trip = Trip.objects.create(distance=distance, fuel_price=fuel_price, fuel_consumption=fuel_consumption)
                result = (float(distance)/100) * float(fuel_consumption) * float(fuel_price)
                print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
                context = {
                    'print_': print_,
                }
                return render(request, 'index.html', context)
            return render(request, 'index.html')

## Дальнейшее развитие:

- **Оптимизация запросов к базе данных.**
- **Реализация отображения истории поездок.**
- **Улучшение дизайна пользовательского интерфейса.**
- **Добавление обработки ошибок и валидации данных.**

## Автор:

- **Андрей Шевелев**