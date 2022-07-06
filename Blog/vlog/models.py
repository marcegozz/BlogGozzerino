from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    etiqueta = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255, default='Sin Categorizar')



#Permite que se lea claramente el titulo y el autor claramente en la pagina de Admin
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('home')


