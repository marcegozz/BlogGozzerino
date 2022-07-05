from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    etiqueta = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()

#Permite que se lea claramente el titulo y el autor claramente en la pagina de Admin
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        #return reverse('ArticuloDetallado', args=(str(self.id)))
        return reverse('home')


