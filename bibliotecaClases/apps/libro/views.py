from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

    
#--- VISTA PARA EL Inicio 
    
class Inicio(TemplateView):
    template_name = 'index.html'

#================================================= AUTORES =================================================

#---VISTA CREAR AUTOR

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

#--- VISTA LISTAR AUTOR
class ListadoAutor(ListView):
    model = Autor
    template_name= 'libro/autor/listar_autor.html'
    context_object_name = 'autores' # opcional, para no tener q llamar de 'object_list' en el template sino de 'autores'
    queryset = Autor.objects.filter(estado=True)
        
#--- VISTA EDITAR AUTOR
class ActualizarAutor(UpdateView):
    model = Autor
    template_name= 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor') #es una forma de redirección

#--- VISTA ELIMINAR AUTOR
class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy('libro:listar_autor')

#--- VISTA DESACTIVAR AUTOR
def desactivarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/autor/desactivar_autor.html',{'autor':autor})

#================================================= LIBROS =================================================
#--- VISTA LISTAR LIBROS
class ListadoLibros(ListView):
    model = Libro
    template_name= 'libro/libros/listar_libro.html'
    context_object_name = 'libros' # opcional, para no tener q llamar de 'object_list' en el template sino de 'libros'
    queryset = Libro.objects.filter(estado=True)

#---VISTA CREAR LIBROS
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libros/crear_libro.html'
    success_url = reverse_lazy('libro:listar_libro')


#--- VISTA EDITAR LIBROS
class ActualizarLibro(UpdateView):
    model = Libro
    template_name= 'libro/libros/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro:listar_libro')


#--- VISTA ELIMINAR LIBROS
class EliminarLibros(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro:listar_libro')

#--- VISTA DESACTIVAR LIBROS
def desactivarLibro(request, id):
    libro = Libro.objects.get(id = id)
    if request.method == 'POST':
        libro.estado = False
        libro.save()
        return redirect('libro:listar_libro')
    return render(request, 'libro/libros/desactivar_libro.html',{'libro': libro})

