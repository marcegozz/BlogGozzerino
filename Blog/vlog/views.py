from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Post
from .forms import PostForm, EditarForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['fecha']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

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

class EliminarPost(DeleteView):
    model = Post
    template_name = 'eliminar.html'
    success_url = reverse_lazy('home')

class AgregarCategoria(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'categoria.html'

def CategoriaVista(request, cat):
    categoria_posts = Post.objects.filter(categoria=cat)
    return render(request, 'categoriasV.html', {'cat': cat.title(), 'categoria_posts': categoria_posts })