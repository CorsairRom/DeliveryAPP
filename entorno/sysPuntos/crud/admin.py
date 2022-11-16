from django.contrib import admin
from .models import cliente, direccion, local, promocion, trabajador, metodo_pago, producto, pedido, detalle_pedido

# Register your models here.
admin.site.register(cliente)
admin.site.register(direccion)
admin.site.register(local)
admin.site.register(promocion)
admin.site.register(metodo_pago)
admin.site.register(trabajador)
admin.site.register(producto)
admin.site.register(pedido)
admin.site.register(detalle_pedido)
