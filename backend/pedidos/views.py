from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pedido
from .serializers import PedidoSerializer
from .notifications import enviar_notificacion_pedido
from django.conf import settings

@api_view(['GET', 'POST'])
def pedidos_list(request):
    if request.method == 'GET':
        estado = request.GET.get('estado')
        pedidos = Pedido.objects.all()

        if estado:
            pedidos = pedidos.filter(estado=estado)

        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save()

            # Preparar datos para notificación
            pedido_data = {
                '_id': str(pedido.id),
                'cliente': {
                    'nombre': pedido.cliente_nombre,
                    'email': pedido.cliente_email,
                },
                'items': pedido.items,
                'total': float(pedido.total),
                'estado': pedido.estado,
            }
            enviar_notificacion_pedido(pedido_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pedido_detail(request, pedido_id):
    try:
        pedido = Pedido.objects.get(pk=pedido_id)
    except Pedido.DoesNotExist:
        return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PedidoSerializer(pedido)
    return Response(serializer.data)

@api_view(['POST'])
def confirmar_pago(request, pedido_id):
    try:
        pedido = Pedido.objects.get(pk=pedido_id)
    except Pedido.DoesNotExist:
        return Response({'error': 'Pedido no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    transaction_id = request.data.get('transaction_id')
    estado = request.data.get('estado', 'pagado')

    pedido.estado = estado
    if transaction_id:
        pedido.transaction_id = transaction_id
    pedido.save()

    serializer = PedidoSerializer(pedido)
    return Response(serializer.data)

@api_view(['POST'])
def crear_pago_epayco(request):
    pedido_data = request.data

    epayco_data = {
        'name': f"Pedido #{pedido_data.get('pedido_id', 'N/A')}",
        'description': 'Compra de productos',
        'invoice': pedido_data.get('pedido_id'),
        'currency': 'COP',
        'amount': str(pedido_data.get('total', 0)),
        'tax_base': '0',
        'tax': '0',
        'country': 'CO',
        'lang': 'es',
        'external': 'false',
        'confirmation': f"{settings.BACKEND_URL}/api/pedidos/confirmar-pago/{pedido_data.get('pedido_id')}/",
        'response': f"{settings.FRONTEND_URL}/pedido/confirmacion",
        'email_billing': pedido_data.get('cliente', {}).get('email', ''),
        'name_billing': pedido_data.get('cliente', {}).get('nombre', ''),
    }

    return Response({
        'checkout_url': 'https://checkout.epayco.co/checkout.js',
        'data': epayco_data
    })
