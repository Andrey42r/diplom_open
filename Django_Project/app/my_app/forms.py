from django import forms
from .models import Trip


class TripForm(forms.Form):
    """
    Форма Django для ввода данных о поездке.
    Эта форма используется для сбора информации о расстоянии, расходе топлива и цене топлива
    от пользователя.  Данные, введенные пользователем, будут использоваться для расчета
    стоимости поездки.
    Fields:
        distance (FloatField): Поле для ввода расстояния поездки (в км).
        fuel_consumption (FloatField): Поле для ввода расхода топлива (л/100км).
        fuel_price (FloatField): Поле для ввода цены топлива (руб/л).
    """
    distance = forms.FloatField()
    fuel_consumption = forms.FloatField()
    fuel_price = forms.FloatField()
