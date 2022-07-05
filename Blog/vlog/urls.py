from django.urls import path
from . import views
from .views import HomeView, ArticuloDetallado

urlpatterns = [
    path('', HomeView.as_view(), name= "home"),
    path('articulo/<int:pk>', ArticuloDetallado.as_view(), name = "ArticuloDetallado"),

]
