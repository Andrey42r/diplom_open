from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Float

# Создаем движок базы данных SQLite; echo=True выводит сгенерированный SQL в консоль.
engine = create_engine("sqlite:///database.db", echo=True)

# Создаем генератор сессий для работы с базой данных.
SessionLocal = sessionmaker(bind=engine)

# Объявляем базовый класс для декларативных моделей SQLAlchemy.
class Base(DeclarativeBase):
    pass


class TripBase(Base):
    __tablename__ = "trip"
    __table_agrs__ = {"extend_existing": True} # Позволяет добавлять новые столбцы в существующую таблицу, не удаляя её.
    distance = Column(Float, primary_key=True) # Расстояние поездки (первичный ключ)
    fuel_consumption = Column(Float) # Расход топлива в литрах на 100 км
    fuel_price = Column(Float) # Цена топлива за литр

# Base.metadata.create_all(bind=engine)