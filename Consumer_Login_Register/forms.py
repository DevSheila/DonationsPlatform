from django.forms import ModelForm
from .models import Consumer
from django.contrib.auth.forms import UserCreationForm

class SingUPForm(UserCreationForm):
    class Meta:
        model = Consumer
        fields = ['Full_name','email','phone_number','Organization','location','category','facebook','Twitter','Website','no_individuals','password1','password2']