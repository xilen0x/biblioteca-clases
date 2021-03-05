from django.urls import path
from .views import CrearAutor, ListadoAutor, EliminarAutor, desactivarAutor, ActualizarAutor
from .views import listarLibro

urlpatterns = [
    path('crear_autor/', CrearAutor.as_view(), name='crear_autor'),
    path('listar_autor/',ListadoAutor.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>',ActualizarAutor.as_view(), name='editar_autor'),
    path('eliminar_autor/<int:pk>',EliminarAutor.as_view(), name='eliminar_autor'),
    path('desactivar_autor/<int:id>',desactivarAutor, name='desactivar_autor'),
    #
    path('listar_libro/',listarLibro, name='listar_libro'),
]