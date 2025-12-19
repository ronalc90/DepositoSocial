import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCarrito } from '../contexts/CarritoContext';
import { pedidosAPI } from '../services/api';
import './Checkout.css';

const Checkout = () => {
  const { items, calcularTotal, limpiarCarrito } = useCarrito();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
    telefono: '',
    direccion: '',
    ciudad: '',
    notas: '',
  });
  const [loading, setLoading] = useState(false);

  const formatPrice = (price) => {
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0,
    }).format(price);
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const pedidoData = {
        cliente: {
          nombre: formData.nombre,
          email: formData.email,
          telefono: formData.telefono,
          direccion: formData.direccion,
          ciudad: formData.ciudad,
        },
        items: items.map((item) => ({
          producto_id: item.producto.id || item.producto._id,
          nombre: item.producto.nombre,
          cantidad: item.cantidad,
          precio: item.producto.precio || 0,
          presentacion: item.presentacion || '',
        })),
        subtotal: calcularTotal(),
        total: calcularTotal(),
        metodo_pago: 'PSE',
        notas: formData.notas,
      };

      const response = await pedidosAPI.create(pedidoData);
      const pedidoId = response.data.id || response.data._id;

      limpiarCarrito();

      navigate(`/pedido/confirmacion?pedido=${pedidoId}`);
    } catch (error) {
      console.error('Error creando pedido:', error);
      alert('Error al procesar el pedido. Por favor intenta nuevamente.');
    } finally {
      setLoading(false);
    }
  };

  if (items.length === 0) {
    navigate('/carrito');
    return null;
  }

  return (
    <div className="checkout">
      <div className="container">
        <h1>Finalizar Compra</h1>

        <div className="checkout-content">
          <form className="checkout-form" onSubmit={handleSubmit}>
            <h2>Información de Contacto</h2>

            <div className="form-group">
              <label>Nombre Completo *</label>
              <input
                type="text"
                name="nombre"
                value={formData.nombre}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label>Email *</label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Teléfono *</label>
                <input
                  type="tel"
                  name="telefono"
                  value={formData.telefono}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>

            <div className="form-group">
              <label>Dirección *</label>
              <input
                type="text"
                name="direccion"
                value={formData.direccion}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Ciudad *</label>
              <input
                type="text"
                name="ciudad"
                value={formData.ciudad}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="form-group">
              <label>Notas (opcional)</label>
              <textarea
                name="notas"
                value={formData.notas}
                onChange={handleInputChange}
                rows="3"
              />
            </div>

            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'Procesando...' : 'Pagar con PSE'}
            </button>
          </form>

          <div className="order-summary">
            <h2>Resumen del Pedido</h2>

            <div className="summary-items">
              {items.map((item, index) => (
                <div key={index} className="summary-item">
                  <span>
                    {item.cantidad}x {item.producto.nombre}
                    {item.presentacion && ` (${item.presentacion})`}
                  </span>
                  <span>{formatPrice((item.producto.precio || 0) * item.cantidad)}</span>
                </div>
              ))}
            </div>

            <div className="summary-total">
              <span>Total</span>
              <span>{formatPrice(calcularTotal())}</span>
            </div>

            <div className="payment-info">
              <p>
                <strong>Método de Pago:</strong> PSE
              </p>
              <p className="payment-note">
                Serás redirigido a la pasarela de pago de ePayco para completar tu compra de forma
                segura.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Checkout;
