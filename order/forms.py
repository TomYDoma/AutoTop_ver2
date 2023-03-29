from django import forms

from accounts.models import Car
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['ID_Car']
