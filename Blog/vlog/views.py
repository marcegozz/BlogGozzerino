from django.shortcuts import render
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Post.model
    template_name: 'home.htlm'