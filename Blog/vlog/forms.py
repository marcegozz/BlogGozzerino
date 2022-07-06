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
        fields = ('titulo', 'etiqueta', 'autor', 'categoria', 'cuerpo')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta' : forms.TextInput(attrs={'class': 'form-control'}),
            'autor' : forms.Select(attrs={'class': 'form-control'}),
            'categoria' : forms.Select(choices=listaOpciones, attrs={'class': 'form-control'}),
            'cuerpo' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditarForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'etiqueta', 'cuerpo')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta' : forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo' : forms.Textarea(attrs={'class': 'form-control'}),
        }
            


#https://getbootstrap.com/docs/5.2/forms/overview/