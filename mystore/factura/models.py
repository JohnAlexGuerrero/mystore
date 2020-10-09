from django.db import models

from bases.models import ClaseModelo
from cliente.models import Cliente
from inventario.models import Producto
from provider.models import Proveedor

# Create your models here.
class Pedido(ClaseModelo):
    referencia = models.CharField(primary_key=True, max_length=40)
    IDproducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    und = models.CharField(max_length=10, help_text='Unidad de Medida',
        null=False, blank=False)
    precio = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return '{}'.format(self.referencia)

    def save(self):
        self.rfv = self.referencia.upper()
        super(Pedido, self)

    class Meta:
        verbose_name_plural= 'Pedidos'


class FacturaCliente(ClaseModelo):
    name = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rfv = models.CharField(max_length=20, unique=True, help_text='Factura de Venta')
    ff = models.DateTimeField(help_text='Fecha de Facturacion')
    fv = models.DateTimeField(help_text='Fecha de vencimiento')
    fp = models.CharField(
        max_length=20,
        help_text='Forma de Pago'
    )
    plazo = models.CharField(max_length=20)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.rfv)

    def save(self):
        self.rfv = self.rfv.upper()
        super(FacturaCliente, self)

    class Meta:
        verbose_name_plural= 'Facturas'

class FacturaProveedor(ClaseModelo):
    name = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    rfv = models.CharField(max_length=20, unique=True, help_text='Factura de Venta')
    ff = models.DateTimeField(help_text='Fecha de Facturacion')
    fv = models.DateTimeField(help_text='Fecha de vencimiento')
    fp = models.CharField(
        max_length=20,
        help_text='Forma de Pago'
    )
    plazo = models.CharField(max_length=20)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.rfv)

    def save(self):
        self.rfv = self.rfv.upper()
        super(FacturaProveedor, self)

    class Meta:
        verbose_name_plural= 'Facturas'
