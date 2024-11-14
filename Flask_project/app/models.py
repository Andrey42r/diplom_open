from datetime import datetime
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