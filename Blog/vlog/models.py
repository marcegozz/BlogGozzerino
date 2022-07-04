from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()

#Permite que se lea claramente el titulo y el autor claramente en la pagina de Admin
    def __str__(self):
        return self.titulo + ' | ' + self.autor


