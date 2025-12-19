from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

@api_view(['GET', 'POST'])
def productos_list(request):
    if request.method == 'GET':
        categoria = request.GET.get('categoria')
        search = request.GET.get('search')
        activo = request.GET.get('activo')

        productos = Producto.objects.all()

        if search:
            productos = productos.filter(
                Q(nombre__icontains=search) |
                Q(descripcion__icontains=search) |
                Q(marca__icontains=search)
            )

        if categoria:
            productos = productos.filter(categoria=categoria)

        if activo is not None:
            activo_bool = activo.lower() == 'true'
            productos = productos.filter(activo=activo_bool)

        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def categorias_list(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
