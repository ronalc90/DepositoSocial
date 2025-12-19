from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos_list, name='productos-list'),
    path('productos/<str:producto_id>/', views.producto_detail, name='producto-detail'),
    path('categorias/', views.categorias_list, name='categorias-list'),
]
