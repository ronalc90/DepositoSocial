from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, blank=True)
    orden = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.CharField(max_length=100)
    subcategoria = models.CharField(max_length=100, blank=True)
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    presentaciones = models.JSONField(default=list, blank=True)
    uso = models.CharField(max_length=100, blank=True)
    caracteristicas = models.JSONField(default=list, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.URLField(max_length=500, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.marca} - {self.nombre}"
