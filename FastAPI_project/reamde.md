# Дипломный проект: Калькулятор стоимости поездки (FastAPI)

Этот проект представляет собой веб-приложение на базе FastAPI, рассчитанное на расчет стоимости поездки, используя локальную базу данных SQLite.

## Функциональность:

- **Расчет стоимости:** Приложение позволяет пользователю ввести расстояние, расход топлива (на 100 км) и цену топлива. На основе этих данных рассчитывается общая стоимость поездки.
- **Сохранение истории поездок:** Приложение сохраняет информацию о поездках в локальной базе данных SQLite.
- **Удобный интерфейс:**  Используется простой и интуитивно понятный веб-интерфейс, созданный с помощью FastAPI и Jinja2 шаблонов.

## Технологии:

- **FastAPI:**  Высокопроизводительный фреймворк для создания веб-приложений на Python.
- **Python:**  Язык программирования.
- **SQLAlchemy:**  ORM для работы с базой данных.
- **Jinja2:** Шаблонизатор для создания HTML-страниц.
- **uvicorn:** Веб-сервер для FastAPI.


## Установка и запуск:

**Предварительные требования:**

- Python 3.x

1. **Клонирование репозитория:**

   ```bash
   git clone https://github.com/Andrey42r/diplom_open.git
   cd diplom_open/FastAPI_project
   
2. **Создание виртуального окружения (рекомендуется):**

       python3 -m venv .venv
       source .venv/bin/activate  # Linux/macOS
       .venv\Scripts\activate  # Windows

3. **Запуск приложения:**

       uvicorn main:app --reload

Приложение будет запущено на http://127.0.0.1:8000/.

Структура проекта:

    main.py: Основной файл приложения FastAPI, содержащий маршруты и логику.
    db_depends.py: Содержит зависимости (например, для базы данных).
    templates/: Директория с HTML-шаблонами.

Примеры кода (фрагменты):

1. Модель Trip ():

         class Trip:
            def __init__(self, distance: float, fuel_consumption: float, fuel_price: float):
                self.distance = distance
                self.fuel_consumption = fuel_consumption
                self.fuel_price = fuel_price

2. Маршрут для расчета стоимости (main.py):

        @app.post("/index")
        async def calculate_trip(request: Request, db: Annotated[Session, Depends(get_db)],
                            distance: float = Form(...),
                            fuel_consumption: float = Form(...),
                            fuel_price: float = Form(...)):
            existing_trip = db.scalar(select(TripBase).where(
                TripBase.distance == distance,
                TripBase.fuel_consumption == fuel_consumption,
                TripBase.fuel_price == fuel_price
            ))

            if existing_trip:
                result = (existing_trip.distance / 100) * existing_trip.fuel_consumption * existing_trip.fuel_price
                print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
            else:
                trip = TripBase(distance=distance, fuel_consumption=fuel_consumption, fuel_price=fuel_price)
                db.add(trip)
                db.commit()
                db.refresh(trip)
                result = (distance / 100) * fuel_consumption * fuel_price
                print_ = f'Стоимость поездки составит {int(result)} рублей! Удачи на дорогах!'
            return templates.TemplateResponse("index.html", {"request": request, "print_": print_})

## Дальнейшее развитие:
- **Оптимизация запросов к базе данных.**
- **Реализация отображения истории поездок.**
- **Улучшение дизайна пользовательского интерфейса.**
- **Добавление обработки ошибок и валидации данных.**
- **Возможность фильтрации/сортировки истории поездок.**


##Автор:
- **Андрей Шевелев**