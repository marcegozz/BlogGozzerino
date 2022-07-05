from tkinter.tix import Select
from turtle import textinput
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'etiqueta', 'autor', 'cuerpo')
        elementos = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'etiqueta' : forms.TextInput(attrs={'class':'form-control'}),
            'autor' : forms.Select(attrs={'class':'form-control'}),
            'cuerpo' : forms.Textarea(attrs={'class':'form-control'}),
        }
            


#https://getbootstrap.com/docs/5.2/forms/form-control/