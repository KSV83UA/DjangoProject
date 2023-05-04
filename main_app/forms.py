from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'e_mail', 'phone', 'date', 'time', 'count_of_people', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ПІБ'}),
            'e_mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пошта', 'value': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон', 'id': 'phone'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата', 'id': 'date'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Час', 'id': 'time'}),
            'count_of_people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кількість людей'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Повідомлення', 'rows': '5'})

        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Ще раз пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpdateOrder(AddOrderForm):
    class Meta:
        model = Clients
        fields = ['count_of_people', 'status']
        widgets = {
            'count_of_people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кількість людей'}),
            'status': forms.TextInput(attrs={'class': 'form-control'})
        }

