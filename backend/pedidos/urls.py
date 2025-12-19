from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedidos_list, name='pedidos-list'),
    path('pedidos/<str:pedido_id>/', views.pedido_detail, name='pedido-detail'),
    path('pedidos/confirmar-pago/<str:pedido_id>/', views.confirmar_pago, name='confirmar-pago'),
    path('pago/epayco/', views.crear_pago_epayco, name='crear-pago-epayco'),
]
