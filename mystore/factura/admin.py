from django.contrib import admin

from .models import Factura, Pedido, ProveedorPedido, ClientePedido

# Register your models here.
admin.site.register(Factura)
admin.site.register(Pedido)
admin.site.register(ProveedorPedido)
admin.site.register(ClientePedido)
