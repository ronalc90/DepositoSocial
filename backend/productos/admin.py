from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'categoria', 'precio', 'activo', 'creado_en']
    list_filter = ['categoria', 'marca', 'activo']
    search_fields = ['nombre', 'descripcion', 'marca']
    list_editable = ['activo']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden']
