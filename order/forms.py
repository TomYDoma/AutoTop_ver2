import datetime

import accounts.models
from django import forms

from accounts.models import Car
from .models import Order



class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class MyTimeInput(forms.DateInput):
    input_type = 'time'
    format = '%H:%M'


class OrderCreateForm(forms.ModelForm):


    client_date = forms.DateField(label='Желаемая дата записи', required=True,
                           widget=MyDateInput({
                               'class': 'inputbox',
                               'id': 'exp_date',
                               'type': 'date',
                               'style': 'width: 20rem'
                           }))

    client_time = forms.TimeField(label='Желаемая дата записи', required=True,
                                  widget=MyTimeInput({
                                      'class': 'inputbox',

                                      'type': 'time',
                                      'style': 'width: 20rem'
                                  }))

    car_mileage = forms.IntegerField(label='Пробег автомобиля')




    class Meta:
        model = Order
        fields = ['ID_Car', 'car_mileage', 'client_date', 'client_time']
