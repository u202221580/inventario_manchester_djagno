from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from inventory.models import Almacen
from .models import Diseno_Color
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


#@login_required
#def inventario(request):
        listar_almacen = Almacen.objects.all()
        listar_diseno = Diseno.objects.all()
        listar_color = Color.objects.all()

def inventario(request):

    rolloss = Rollos.objects.all()
    
    return render(request, 'inventario.html', {'data': rolloss})
    """
    context = {}
    context['form'] = AlmacenForm
    return render(request, 'inventario.html', context)

    
    listar_almacen = Almacen.objects.all()
    listar_diseno = Diseno.objects.all()
    listar_color = Color.objects.all()
    rolloss = Rollos.objects.all()
    
    return render(request, 'inventario.html', {'data': rolloss, "data_almacen": listar_almacen, 
                                "data_diseno": listar_diseno, "data_color": listar_color})
    """



#def listarcampos(request):
#    listar_almacen = Almacen.objects.all()
#    listar_diseno = Diseno.objects.all()
#    listar_color = Color.objects.all()

#    return render(request, 'inventario.html', {"data_almacen": listar_almacen, 
#                            "data_diseno": listar_diseno, "data_color": listar_color})

"""
@login_required
def dropdownsearch(request):  
        listar_almacen = Almacen.objects.all()
        listar_diseno = Diseno.objects.all()
        listar_color = Color.objects.all()

        return redirect(request, 'inventario' ,{"data_almacen": listar_almacen, 
                                "data_diseno": listar_diseno, "data_color": listar_color})
    if request.method=="POST":
        
        searchalmacen=request.POST.get('almacen')
        searchdiseno=request.POST.get('diseno')
        searchcolor=request.POST.get('color')
        rollosearch=Rollos.objects.filter(almacen=searchalmacen,diseno=searchdiseno,color=searchcolor)
          
        return render(request,'inventario.html',{"data":rollosearch})
    else:   


            displayrollos=Rollos.objects.all()
          
            return render(request,'inventario.html',{"data":displayrollos})
"""


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
            return redirect('CRUD')
        except ValueError:
            return render(request, 'rollo_detail.html', {
                'rollos': rollos, 
                'form': form, 
                'error': 'Error updating task'})
        

@login_required
def CRUD(request):
    rolloss = Rollos.objects.all()
    return render(request, 'crud.html', {'rolloss': rolloss})




@login_required       
def create_rollo(request):
        if request.method == 'GET':
            return render(request, 'crud.html', {
            'form': RollosForm})
        else:
            try:
                form = RollosForm(request.POST)
                newrollo = form.save(commit=True)
                newrollo.user = request.user
                newrollo.save()
                return redirect('CRUD')
            except ValueError:
                return render(request, 'crud.html', {
                'form': RollosForm,
                'error': 'Please provide valide data'
            })