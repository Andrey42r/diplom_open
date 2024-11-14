from django import forms
from .models import Trip

class TripForm(forms.Form):
    distance = forms.FloatField()
    fuel_consumption = forms.FloatField()
    fuel_price = forms.FloatField()