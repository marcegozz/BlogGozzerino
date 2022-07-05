from django.urls import path
from .views import HomeView, ArticuloDetallado, AgregarPost, EditarPost, EliminarPost

urlpatterns = [
    path('', HomeView.as_view(), name= "home"),   #No utilice '/' al ser innecesario segun el programa
    path('articulo/<int:pk>', ArticuloDetallado.as_view(), name = "ArticuloDetallado"),
    path('agregar_post/', AgregarPost.as_view(), name = "AgregarPost"),
    path('articulo/editar/<int:pk>', EditarPost.as_view(), name = "EditarPost"),
    path('articulo/<int:pk>/eliminar', EliminarPost.as_view(), name= "EliminarPost" )
]
