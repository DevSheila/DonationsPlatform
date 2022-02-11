import email
from django.shortcuts import render, redirect
from .forms import SingUPForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .models import Donor


def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try: 
            user = Donor.objects.get(email=email)

        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'User or password is incorrect')

    context = {'page': page}

    return render(request, 'login_register.html', context)
def LogoutUser(request):

    logout(request)
    return redirect('home')
def RegisterUser(request):
    form = SingUPForm()
    if request.method == "POST":
        form = SingUPForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, " Error ") 

    return render(request, 'login_register.html',{'form': form})
    

def home(request):

    return render(request, 'home.html')
    