from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditarForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticuloDetallado(DetailView):
    model = Post
    template_name = 'articulo.html'

class AgregarPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postear.html'

class EditarPost(UpdateView):
    model = Post
    form_class = EditarForm
    template_name = 'editar.html'