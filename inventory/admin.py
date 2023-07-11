from django.contrib import admin
from .models import Almacen
from .models import Diseno_Color
from .models import Rollos

# Register your models here.
admin.site.register(Almacen)

admin.site.register(Diseno_Color)

admin.site.register(Rollos)

