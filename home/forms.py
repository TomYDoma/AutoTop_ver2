from form import form
from django import forms

from .models import FeedbackList, Comment
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


class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=200, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Текст комментария',
                                                              'class': 'form-control',
                                                              }))

    class Meta:
        model = Comment
        fields = ('content',)

