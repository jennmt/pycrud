from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

fecha_actual = datetime.now()

def home(request):
    return render(request, 'inicio.html', {
        'fecha_actual': fecha_actual
    })

def signup(request):
    # print(request.POST)
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'inicio.html')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'No coinciden las contraseñas'
                })
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectas'
            }) 
        else:
            login(request, user)
            return redirect('home')
        
def signout(request):
    logout(request)
    return redirect('home')

def tasks(request):
    return render(request, 'tasks.html')