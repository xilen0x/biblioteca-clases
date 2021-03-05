from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 200, blank = False, null = False)
    apellidos = models.CharField('Apellidos', max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripción', blank = True, null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] # para ordenar por nombre los autores (en el admin)

    def __str__(self):
        template = '{0.nombre} {0.apellidos}' #así indico q me muestre el nombre y apellido en lugar de 'object(1)..(algo asi) en el admin
        return template.format(self)

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 200, blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', max_length = 200, blank = False, null = False)
    #autor_id = models.OneToOneField(Autor, on_delete = models.CASCADE) # relacion uno a uno
    #autor_id = models.ForeignKey(Autor, on_delete = models.CASCADE) # relacion uno a muchos
    autor_id = models.ManyToManyField(Autor) # relacion muchos a muchos
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        template = '{0.titulo}'
        return template.format(self)
