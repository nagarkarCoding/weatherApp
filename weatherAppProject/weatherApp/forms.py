# weatherApp/forms.py
from django import forms

class WeatherSearchForm(forms.Form):
    city = forms.CharField(
        label='city',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter city name'})
    )
