
from app import db

class Trip(db.Model):
    """
    Модель SQLAlchemy для представления поездки.

    Сохраняет информацию о поездке, включая расстояние, расход топлива и цену топлива.
    Связана с таблицей 'trip' в базе данных.

    Attributes:
        distance (db.Float): Расстояние поездки (в километрах).
        fuel_consumption (db.Float): Расход топлива (в литрах на 100 км).
        fuel_price (db.Float): Цена топлива (в рублях за литр).
    """
    __tablename__ = 'trip'

    distance = db.Column(db.Float)
    fuel_consumption = db.Column(db.Float)
    fuel_price = db.Column(db.Float)

    def __init__(self, distance, fuel_consumption, fuel_price):
        """
        Инициализирует объект Trip.

        Args:
            distance (float): Расстояние поездки.
            fuel_consumption (float): Расход топлива.
            fuel_price (float): Цена топлива.
        """
        self.distance = distance
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def __repr__(self):
        """
        Возвращает строковое представление объекта Trip.

        Returns:
            str: Строка, представляющая объект Trip.
        """
        return '<Trip %r>' % (self.distance)