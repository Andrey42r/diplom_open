from django.db import models

# Create your models here.

class Trip(models.Model):
    """
    Модель для хранения информации о поездке.

    Attributes:
        distance (FloatField): Расстояние поездки в километрах.  Значение по умолчанию 0, допускаются NULL значения.
        fuel_consumption (FloatField): Расход топлива в литрах на 100 км. Значение по умолчанию 0, допускаются
        NULL значения.
        fuel_price (FloatField): Цена топлива за литр. Значение по умолчанию 0, допускаются NULL значения.

    """
    distance = models.FloatField(default=0, null=True)
    fuel_consumption = models.FloatField(default=0, null=True)
    fuel_price = models.FloatField(default=0, null=True)

