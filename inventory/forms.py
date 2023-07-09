from django import forms
from .models import Almacen
from .models import Diseno
from .models import Color
from .models import Rollos

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del almacen'})
        }

class DisenoForm(forms.ModelForm):
    class Meta:
        model = Diseno
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del diseño'})
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del color'})
        }

class RollosForm(forms.ModelForm):
    class Meta:
        model = Rollos
        fields = ['almacen', 'diseno', 'color','metros']
        widgets = {
            'almacen': forms.CheckboxSelectMultiple(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Seleccione almacen'}),
            'diseno': forms.CheckboxSelectMultiple(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Seleccione diseño'}),
            'color': forms.CheckboxSelectMultiple(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Seleccione color'}),
            'metros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese metraje'})
        }