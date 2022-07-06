from django import forms
from .models import Post, Categoria

#Para que saque la información de la DB
opciones = Categoria.objects.all().values_list('nombre','nombre')

listaOpciones = []

for item in opciones:
    listaOpciones.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'etiqueta', 'autor', 'categoria', 'detalle', 'cuerpo', 'header_img')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta' : forms.TextInput(attrs={'class': 'form-control'}),
            'autor' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'kiki', 'type':'hidden'}), #Kiki es el nombre de mi gata :)
            'categoria' : forms.Select(choices=listaOpciones, attrs={'class': 'form-control'}),
            'detalle' : forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escribe una breve descripción de tu Post.'}),
            'cuerpo' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditarForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'etiqueta', 'detalle', 'cuerpo')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta' : forms.TextInput(attrs={'class': 'form-control'}),
            'detalle' : forms.Textarea(attrs={'class': 'form-control'}),
            'cuerpo' : forms.Textarea(attrs={'class': 'form-control'}),
        }
            


#https://getbootstrap.com/docs/5.2/forms/overview/