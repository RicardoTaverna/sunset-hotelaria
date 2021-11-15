from django.contrib import admin
from .models import Cliente, Apartamento, Reserva, Produto_Cliente, Produto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Apartamento)
admin.site.register(Reserva)
admin.site.register(Produto_Cliente)
admin.site.register(Produto)
