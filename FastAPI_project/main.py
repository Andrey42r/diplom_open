from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.db import TripBase
from backend.db_depends import get_db
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class Trip:
    def __init__(self, distance: float, fuel_consumption: float, fuel_price: float):
        self.distance = distance
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price


@app.get("/")
async def menu(request: Request):
    """
        Обработчик GET-запроса для отображения меню.

        Args:
            request (Request): Объект запроса FastAPI.

        Returns:
            HTMLResponse: Ответ с шаблоном меню.
        """
    return templates.TemplateResponse("menu.html", {"request": request})


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    """
        Обработчик GET-запроса для отображения главной страницы.

        Args:
            request (Request): Объект запроса FastAPI.

        Returns:
            HTMLResponse: Ответ с главной страницей.
        """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/index")
async def calculate_trip(request: Request, db: Annotated[Session, Depends(get_db)],
                         distance: float = Form(...),
                         fuel_consumption: float = Form(...),
                         fuel_price: float = Form(...)):
    """
       Обработчик POST-запроса для расчета стоимости поездки.

       Args:
           request (Request): Объект запроса FastAPI.
           db (Session): Объект сессии базы данных.
           distance (float): Расстояние поездки.
           fuel_consumption (float): Расход топлива.
           fuel_price (float): Цена топлива.

       Returns:
           HTMLResponse: Ответ с результатом расчета.
       """
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
