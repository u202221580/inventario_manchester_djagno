from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Almacen
from .models import Diseno
from .models import Color
from .models import Rollos
from .forms import RollosForm


# Create your views here.
def home(request):    
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                email = request.POST['email'],                                                
                password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inventario')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Password do not match'
                    })

@login_required
def singout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
            password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('inventario')

@login_required
def inventario(request):
    rolloss = Rollos.objects.all()
    return render(request, 'inventario.html', {'rolloss': rolloss})


@login_required
def rollo_detail(request, rollo_id):
    if request.method == 'GET':
        rollos = get_object_or_404(Rollos, pk=rollo_id)
        form = RollosForm(instance=rollos)
        return render(request, 'rollo_detail.html', {
            'rollos': rollos, 
            'form': form})
    else:
        try:
            rollos = get_object_or_404(Rollos, pk=rollo_id)
            form = RollosForm(request.POST, instance=rollos)
            form.save()
            return redirect('inventario')
        except ValueError:
            return render(request, 'rollo_detail.html', {
                'rollos': rollos, 
                'form': form, 
                'error': 'Error updating task'})