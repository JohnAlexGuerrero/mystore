from django.db import models

from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=40, help_text='Descripcion de la Categoria',
    unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self)

    class Meta:
        verbose_name_plural= 'Categorias'

class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, help_text='Descripcion de la Categoria',
        unique=True)
    existencia = models.IntegerField(default=0)
    marca = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self)

    class Meta:
        verbose_name_plural= 'Productos'
        #unique_together = ('codigo','codigo de barra')