# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

class Datousuario(models.Model):
    usuario= models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField(blank=True, null=True)
    pais= models.CharField(max_length=50, blank=True)
    fecha_nacimiento= models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.usuario.username
    