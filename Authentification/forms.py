from django.forms import ModelForm
from .models import AllUsers
from django.contrib.auth.forms import UserCreationForm

class SingUPForm(UserCreationForm):
    class Meta:
        model = AllUsers
        fields = ['Full_name','email','phone_number','sign_up_as','Organization','donee_name','donee_category','no_individuals','facebook','twitter','website','location','password1','password2']