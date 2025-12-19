from django.db import models

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente_nombre = models.CharField(max_length=200)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=50)
    cliente_direccion = models.TextField()
    cliente_ciudad = models.CharField(max_length=100)

    items = models.JSONField(default=list)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    metodo_pago = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=200, blank=True)
    notas = models.TextField(blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ['-creado_en']

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nombre}"
