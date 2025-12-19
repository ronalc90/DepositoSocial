from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id', 'cliente', 'items', 'subtotal', 'total', 'estado',
            'metodo_pago', 'transaction_id', 'notas', 'creado_en', 'actualizado_en',
            'cliente_nombre', 'cliente_email', 'cliente_telefono',
            'cliente_direccion', 'cliente_ciudad'
        ]
        read_only_fields = ['creado_en', 'actualizado_en', 'estado']
        extra_kwargs = {
            'cliente_nombre': {'write_only': True, 'required': False},
            'cliente_email': {'write_only': True, 'required': False},
            'cliente_telefono': {'write_only': True, 'required': False},
            'cliente_direccion': {'write_only': True, 'required': False},
            'cliente_ciudad': {'write_only': True, 'required': False},
        }

    def get_cliente(self, obj):
        return {
            'nombre': obj.cliente_nombre,
            'email': obj.cliente_email,
            'telefono': obj.cliente_telefono,
            'direccion': obj.cliente_direccion,
            'ciudad': obj.cliente_ciudad,
        }

    def create(self, validated_data):
        if 'cliente' in self.initial_data:
            cliente = self.initial_data['cliente']
            validated_data['cliente_nombre'] = cliente.get('nombre', '')
            validated_data['cliente_email'] = cliente.get('email', '')
            validated_data['cliente_telefono'] = cliente.get('telefono', '')
            validated_data['cliente_direccion'] = cliente.get('direccion', '')
            validated_data['cliente_ciudad'] = cliente.get('ciudad', '')

        return super().create(validated_data)
