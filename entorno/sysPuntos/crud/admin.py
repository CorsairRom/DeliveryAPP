from django.contrib import admin
from .models import cliente, direccion, local, promocion

# Register your models here.
admin.site.register(cliente)
admin.site.register(direccion)
admin.site.register(local)
admin.site.register(promocion)
