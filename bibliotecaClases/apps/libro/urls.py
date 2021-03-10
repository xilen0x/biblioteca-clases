from django.urls import path
from django.contrib.auth.decorators import login_required #para bloquear acceso a rutas de los no logueados
from .views import CrearAutor, ListadoAutor, ActualizarAutor, EliminarAutor, desactivarAutor
from .views import ListadoLibros, CrearLibro, ActualizarLibro, EliminarLibros, desactivarLibro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('crear_autor/', login_required(CrearAutor.as_view()), name='crear_autor'),
    path('listar_autor/',login_required(ListadoAutor.as_view()), name='listar_autor'),
    path('editar_autor/<int:pk>/',login_required(ActualizarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>/',login_required(EliminarAutor.as_view()), name='eliminar_autor'),
    path('desactivar_autor/<int:id>/',login_required(desactivarAutor), name='desactivar_autor'),
    
    path('listar_libro/',login_required(ListadoLibros.as_view()), name='listar_libro'),
    path('crear_libro/',login_required(CrearLibro.as_view()), name='crear_libro'),
    path('editar_libro/<int:pk>/',login_required(ActualizarLibro.as_view()), name='editar_libro'),
    path('eliminar_libro/<int:pk>/',login_required(EliminarLibros.as_view()), name='eliminar_libro'),
    path('desactivar_libro/<int:id>/',login_required(desactivarLibro), name='desactivar_libro'),
    
]