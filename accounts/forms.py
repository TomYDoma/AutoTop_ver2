from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Car


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))


    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя',
                                                               'class': 'login-field-icon fui-user',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                              'class': 'login-field-icon fui-user',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Никнейм',
                                                             'class': 'login-field-icon fui-user',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Электронная почта',
                                                           'class': 'login-field-icon fui-user',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                  'class': 'login-field-icon fui-user',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля',
                                                                  'class': 'login-field-icon fui-user',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))



    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    middleName = forms.CharField(max_length=100,
                                  required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Отчество',
                                                                'class': 'form-control',
                                                                }))
    addres = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Адрес',
                                                               'class': 'form-control',
                                                               }))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    numberPhone = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Телефон',
                                                              'class': 'form-control',
                                                              }))

    class Meta:
        model = Profile
        fields = ['avatar', 'middleName', 'addres', 'bio', 'numberPhone']




###### Форма для добавления машины
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Car_Brand', 'Car_Model', 'image', 'mileage', 'PTS', 'State_Number', 'VIN', 'typeCar', 'Color', 'Relese_Date']


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Car_Brand', 'Car_Model', 'image', 'mileage', 'PTS', 'State_Number', 'VIN', 'typeCar', 'Color', 'Relese_Date']