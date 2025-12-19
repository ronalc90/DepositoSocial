import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useCarrito } from '../contexts/CarritoContext';
import './Carrito.css';

const Carrito = () => {
  const { items, actualizarCantidad, eliminarItem, calcularTotal } = useCarrito();
  const navigate = useNavigate();

  const formatPrice = (price) => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0,
    }).format(price);
  };

  const handleCheckout = () => {
    navigate('/checkout');
  };

  if (items.length === 0) {
    return (
      <div className="carrito-vacio">
        <div className="container">
          <h2>Tu carrito está vacío</h2>
          <p>Agrega productos para comenzar tu compra</p>
          <Link to="/" className="btn-primary">
            Ver Catálogo
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="carrito">
      <div className="container">
        <h1>Carrito de Compras</h1>

        <div className="carrito-content">
          <div className="carrito-items">
            {items.map((item, index) => (
              <div key={index} className="carrito-item">
                <div className="item-image">
                  {item.producto.imagen ? (
                    <img src={item.producto.imagen} alt={item.producto.nombre} />
                  ) : (
                    <div className="no-image">📦</div>
                  )}
                </div>

                <div className="item-info">
                  <h3>{item.producto.nombre}</h3>
                  <p className="item-brand">{item.producto.marca}</p>
                  {item.presentacion && <p className="item-presentacion">{item.presentacion}</p>}
                </div>

                <div className="item-quantity">
                  <button onClick={() => actualizarCantidad(index, item.cantidad - 1)}>-</button>
                  <span>{item.cantidad}</span>
                  <button onClick={() => actualizarCantidad(index, item.cantidad + 1)}>+</button>
                </div>

                <div className="item-price">
                  {formatPrice((item.producto.precio || 0) * item.cantidad)}
                </div>

                <button className="item-remove" onClick={() => eliminarItem(index)}>
                  ✕
                </button>
              </div>
            ))}
          </div>

          <div className="carrito-summary">
            <h2>Resumen del Pedido</h2>

            <div className="summary-row">
              <span>Subtotal</span>
              <span>{formatPrice(calcularTotal())}</span>
            </div>

            <div className="summary-row total">
              <span>Total</span>
              <span>{formatPrice(calcularTotal())}</span>
            </div>

            <button className="checkout-btn" onClick={handleCheckout}>
              Proceder al Pago
            </button>

            <Link to="/" className="continue-shopping">
              Continuar Comprando
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Carrito;
