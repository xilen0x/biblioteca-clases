from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor, Libro
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy
#-------------------------------------------- VISTA PARA EL Inicio ------------------------------------#

class Inicio(TemplateView):
    template_name = 'index.html'
        
#=================================================AUTORES=================================================

#-------------------------------------------- VISTA CREAR AUTOR------------------------------------#
'''  # vista basada en funcion
    def crearAutor(request):
    if request.method == 'POST':#si el metodo por el q viene el request es post entonces ...
        autor_form = AutorForm(request.POST) # instancio AutorForm el archivo forms y le paso los datos q estan en el request.post
        if autor_form.is_valid():  # Si los datos están correctos,() con la funcion is_valid)...
            autor_form.save() #guardamos en la BD los datos.
            return redirect('index') # ahora redirecciono al usuario.
    else:
        autor_form = AutorForm() # si el metodo no es post, instancio de igual manera el formulario pero sin datos y...
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form}) ''' # pido q renderice el formulario vacío(osea cuando ingresa a esta pág).

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

#-------------------------------------------- VISTA LISTAR AUTOR------------------------------------#
""" # vista basada en funcion
    def listarAutor(request):
    #autores = Autor.objects.all() #consulta orm para traer toda la info de la clase Autor (modelo)
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autor.html', {'autores':autores}) # pido q renderice en listar_autor.html la info de la var. autores """

# vista basada en clase
class ListadoAutor(ListView):
    model = Autor
    template_name= 'libro/listar_autor.html'
    context_object_name = 'autores' # opcional, para no tener q llamar de 'object_list' en el template sino de 'autores'
    queryset = Autor.objects.filter(estado=True)
    

#-------------------------------------------- VISTA EDITAR AUTOR------------------------------------#
''' # vista basada en funcion
    def editarAutor(request, id):#asumiendo q nuestra PK tiene como nombre id
    autor_form = None
    error = None
    try: #intenta hacer esto o de lo contrario lanza la excepción (except)
        autor = Autor.objects.get(id = id) #traemos el registro q coincida con el id q se nos requiere.
        if request.method == 'GET': #osea si se obtuvo la info pero aun no se ha modificado...
            autor_form = AutorForm(instance = autor) #traemos el formulario con los datos
        else:
            autor_form = AutorForm(request.POST, instance = autor) #de lo contrario, como es POST, verificamos y guardamos.
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')


    except ObjectDoesNotExist as e:# en caso de querer editar un id inexistente, renderizamos el error
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form, 'error':error}) '''


#vista basada en clase
class ActualizarAutor(UpdateView):
    model = Autor
    template_name= 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor') #es una forma de redirección

#-------------------------------------------- VISTA ELIMINAR AUTOR------------------------------------#

''' def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id)

    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html',{'autor':autor}) '''

class EliminarAutor(DeleteView):
    model = Autor
    success_url = reverse_lazy('libro:listar_autor')
#-------------------------------------------- VISTA DESACTIVAR AUTOR------------------------------------#

def desactivarAutor(request, id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/desactivar_autor.html',{'autor':autor})

#=================================================LIBROS=================================================
def listarLibro(request):
    #autores = Autor.objects.all() #consulta orm para traer toda la info de la clase Autor (modelo)
    libros = Libro.objects.all()
    return render(request, 'libro/listar_libro.html', {'libros':libros})
    













