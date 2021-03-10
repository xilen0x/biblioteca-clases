from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre': 'Nombre del autor:',
            'apellidos': 'Apellidos del autor:',
            'nacionalidad': 'Nacionalidad del autor:',
            'descripcion': 'Pequeña descripción:',
        }
        #estilos q se pueden config. desde aqui al formulario:
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del Autor'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del Autor'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la nacionalidad'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción'
                }
            )
        }

        
        
class LibroForm(forms.ModelForm):
        
    class Meta:
        model = Libro
        fields = ['titulo','autor_id','fecha_publicacion']
        labels = {
            'titulo': 'Titulo del libro:',
            'autor_id': 'Autor:',
            'fecha_publicacion': 'Fecha de Publicación:',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el titulo del libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control',
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(),
        }