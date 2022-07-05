from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticuloDetallado(DetailView):
    model = Post
    template_name = 'articulo.html'

class AgregarPost(CreateView):
    model = Post
    template_name = 'postear.html'
    fields = '__all__'