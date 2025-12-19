from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente_nombre', 'total', 'estado', 'metodo_pago', 'creado_en']
    list_filter = ['estado', 'metodo_pago', 'creado_en']
    search_fields = ['cliente_nombre', 'cliente_email', 'transaction_id']
    readonly_fields = ['creado_en', 'actualizado_en']
