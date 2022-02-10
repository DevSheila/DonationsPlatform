from django.forms import ModelForm
from .models import Donor
from django.contrib.auth.forms import UserCreationForm

class SingUPForm(UserCreationForm):
    class Meta:
        model = Donor
        fields = ['Full_name','email','phone_number','Organization','location','password1','password2']