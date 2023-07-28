from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username  = forms.CharField(max_length=200, label="Full Name", widget=forms.TextInput(attrs={"placeholder":'Enter Your Full Name'}))
    password = forms.CharField(max_length=255, label="Token ID", widget=forms.TextInput(attrs={"placeholder":'Enter Your Token id'}))
    
    class Meta:
        fields= ("password")

       
       
class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class ProductForm (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user']


class TrackingForm (ModelForm):
    class Meta:
        model = Tracking
        fields = '__all__'
        exclude = ['user']

class Step4Form (ModelForm):
    class Meta:
        model = Step4
        fields = '__all__'
        exclude = ['user']

class Step5Form (ModelForm):
    class Meta:
        model = Step5
        fields = '__all__'
        exclude = ['user']

class Step6Form (ModelForm):
    class Meta:
        model = Step6
        fields = '__all__'
        exclude = ['user']