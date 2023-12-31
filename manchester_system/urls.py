"""
URL configuration for manchester_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.singout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('pagina/', views.pagina, name='pagina'),
    
    path('inventario/', views.inventario, name='inventario'),
    path('inventario/<int:rollo_id>/', views.rollo_detail, name='rollo_detail'),
    path('CRUD/', views.CRUD, name='CRUD'),
    path('CRUD/', views.create_rollo, name='create_rollo'),
    #path('inventario/', views.dropdownsearch, name="dropdownsearch"),
    #path('inventario/', views.listarcampos, name="listarcampos"),
    

]
