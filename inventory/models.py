from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Almacen(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Diseno(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Rollos(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    diseno = models.ForeignKey(Diseno, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    metros = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.almacen.name + " | " + self.diseno.name + "-" + self.color.name + " | " + self.metros
    
