from django.db import models

from bases.models import ClaseModelo
# Create your models here.
class Cliente(ClaseModelo):
    name = models.CharField(max_length=100, help_text='Nombre de Cliente')
    IDcliente = models.CharField(
        max_length=50,
        help_text='Nit / Cc',
        unique=True)
    direccion = models.CharField(
        max_length=250,
        null=True, blank=True
    )
    telefono = models.CharField(
        max_length=100,
        null=True, blank=True
    )
    email = models.CharField(
        max_length=250,
        null=True, blank=True
    )
    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        self.name = self.name.upper()
        super(Cliente, self).save()
    
    class Meta:
        verbose_name_plural = 'Clientes'