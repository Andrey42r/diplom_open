from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, Float

engine = create_engine("sqlite:///database.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class TripBase(Base):
    __tablename__ = "trip"
    __table_agrs__ = {"extend_existing": True}
    distance = Column(Float, primary_key=True)
    fuel_consumption = Column(Float)
    fuel_price = Column(Float)

# Base.metadata.create_all(bind=engine)