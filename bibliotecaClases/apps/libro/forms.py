from django import forms
from .models import Autor

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