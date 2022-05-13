from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def index(request):
    hotels = Hotel_Branches.objects.all()
    context = {'hotels':hotels}
    return render(request, 'dbcep/index.html',context)

def reservation(request):
    books = Booking.objects.all()
    context1 = {'books':books}
    return render(request, 'dbcep/reservation.html',context1)


def about(request):
    return render(request,'dbcep/about.html')

def contact(request):
    return render(request,'dbcep/contact.html')

def gallery(request):
    return render(request,'dbcep/gallery.html')

def menu(request):
    return render(request,'dbcep/menu.html')



def signup_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'dbcep/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'dbcep/signup.html', {'form': form})

def signin_user(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'dbcep/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'dbcep/signin.html', {'form': form})



def signout_user(request):
    logout(request)
    return redirect('/')

    