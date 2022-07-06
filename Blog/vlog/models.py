from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    header_img = models.ImageField(upload_to="imagenes/",blank=True, null=True,)
    etiqueta = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255, default='Sin Categorizar')
    detalle = models.CharField(max_length=255)



#Permite que se lea claramente el titulo y el autor claramente en la pagina de Admin
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('home')


