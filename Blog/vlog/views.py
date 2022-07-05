from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticuloDetallado(DetailView):
    model = Post
    template_name = 'articulo.html'