from django.contrib import admin
from .models import Almacen
from .models import Diseno
from .models import Color
from .models import Rollos

# Register your models here.
admin.site.register(Almacen)

admin.site.register(Diseno)

admin.site.register(Color)

admin.site.register(Rollos)

