from .models import FeedbackList
from django.forms import ModelForm, TextInput



class FeedbackListForm(ModelForm):
    class Meta:
        model = FeedbackList
        fields = ('name', 'email', 'number')

        widgets = {
            "name": TextInput(attrs={
                "type" :"name",
                "class":"form-control",
                "placeholder":"Ваше имя"

            }),
            "email": TextInput(attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "name@example.com"
            }),
            "number": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ваш телефон"
            })
        }