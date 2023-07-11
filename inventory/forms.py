from django import forms
from .models import Almacen
from .models import Diseno_Color
from .models import Rollos

class AlmacenForm(forms.Form):
    state = forms.ChoiceField(
        choices = Almacen,
        label='Almacen'
    )
    class Meta:
        fields = ['state',]

class Diseno_ColorForm(forms.ModelForm):
    class Meta:
        model = Diseno_Color
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del diseño y color'})
        }


class RollosForm(forms.ModelForm):
    class Meta:
        model = Rollos
        fields = ['codigo','almacen', 'diseno_color','metros']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Ingrese codigo'}),
            'almacen': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Seleccione almacen'}),
            'diseno_color': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', 'placeholder': 'Seleccione diseño y color'}),            
            'metros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese metraje'})
        }