# Дипломный проект: Калькулятор стоимости поездки (Flask)

Этот проект представляет собой веб-приложение на базе Flask для расчета стоимости поездки, используя локальную базу данных SQLite.

## Функциональность:

- **Расчет стоимости:** Приложение позволяет пользователю ввести расстояние, расход топлива (на 100 км) и цену топлива. На основе этих данных рассчитывается общая стоимость поездки.
- **Сохранение истории поездок:** Приложение сохраняет информацию о поездках в локальной базе данных SQLite.
- **Удобный интерфейс:**  Используется веб-интерфейс, созданный с помощью шаблонов Jinja2, позволяющий пользователю вводить данные и видеть результат.


## Технологии:

- **Flask:** Веб-фреймворк для Python.
- **Python:** Язык программирования.
- **Jinja2:** Шаблонизатор для HTML-страниц.
- **sqlite3:**  Драйвер для работы с SQLite.


## Установка и запуск:

**Предварительные требования:**

- Python 3.x
- Flask

1. **Клонирование репозитория:**

   ```bash
   git clone https://github.com/Andrey42r/diplom_open.git
   cd diplom_open/Flask_project/app
   
2. **Создание виртуального окружения (рекомендуется):**

       python3 -m venv .venv
       source .venv/bin/activate  # Linux/macOS
       .venv\Scripts\activate  # Windows

3. Запуск приложения:

       python app.py

Приложение будет запущено на http://127.0.0.1:5000/.

Структура проекта:

    app.py: Главный файл приложения Flask, содержащий маршруты и логику.
    models.py: Определяет модели SQlite для работы с базой данных.
    templates/: Директория с HTML-шаблонами.

Примеры кода (фрагменты):
1. Модель Trip (models.py, пример):

        from app import db

        class Trip(db.Model):
            __tablename__ = 'trip'

            distance = db.Column(db.Float)
            fuel_consumption = db.Column(db.Float)
            fuel_price = db.Column(db.Float)

            def __init__(self, distance, fuel_consumption, fuel_price):
                self.distance = distance
                self.fuel_consumption = fuel_consumption
                self.fuel_price = fuel_price

            def __repr__(self):
                return '<Trip %r>' % (self.distance)

2. Маршрут для расчета стоимости (app.py, пример):

         import sqlite3
         import os
         from flask import Flask, render_template, request


        @app.route('/index/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
            distance = request.form["distance"]
            fuel_consumption = request.form["fuel_consumption"]
            fuel_price = request.form["fuel_price"]
            conn = connect_db()
            conn.execute('INSERT INTO trip (distance, fuel_consumption, fuel_price) VALUES (?, ?, ?)',
                        (distance, fuel_consumption, fuel_price))
            conn.commit()
            conn.close()
            result = (float(distance)/100) * float(fuel_consumption) * float(fuel_price)
            print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
            return render_template('index.html', print_=print_)

        return render_template('index.html')    

## Дальнейшее развитие:

- **Оптимизация запросов к базе данных.**
- **Реализация отображения истории поездок.**
- **Улучшение дизайна пользовательского интерфейса.**
- **Добавление обработки ошибок и валидации данных.**

## Автор:

- **Андрей Шевелев**