import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { productosAPI } from '../services/api';
import { useCarrito } from '../contexts/CarritoContext';
import Toast from '../components/Toast';
import './ProductDetail.css';

const ProductDetail = () => {
  const { id } = useParams();
  const [producto, setProducto] = useState(null);
  const [loading, setLoading] = useState(true);
  const [cantidad, setCantidad] = useState(1);
  const [presentacionSeleccionada, setPresentacionSeleccionada] = useState('');
  const [showToast, setShowToast] = useState(false);
  const { agregarItem } = useCarrito();

  useEffect(() => {
    const fetchProducto = async () => {
      try {
        const response = await productosAPI.getById(id);
        setProducto(response.data);
        if (response.data.presentaciones && response.data.presentaciones.length > 0) {
          setPresentacionSeleccionada(response.data.presentaciones[0]);
        }
      } catch (error) {
        console.error('Error cargando producto:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProducto();
  }, [id]);

  const formatPrice = (price) => {
    if (!price) return 'Consultar precio';
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0,
    }).format(price);
  };

  const handleAgregarCarrito = () => {
    agregarItem(producto, cantidad, presentacionSeleccionada);
    setShowToast(true);
  };

  if (loading) {
    return <div className="loading">Cargando...</div>;
  }

  if (!producto) {
    return <div className="error">Producto no encontrado</div>;
  }

  return (
    <div className="product-detail">
      <div className="container">
        <div className="detail-grid">
          <div className="product-image-large">
            {producto.imagen ? (
              <img src={producto.imagen} alt={producto.nombre} />
            ) : (
              <div className="no-image-large">
                <svg width="200" height="200" viewBox="0 0 24 24" fill="none">
                  <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" strokeWidth="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5" fill="currentColor"/>
                  <path d="M21 15l-5-5L5 21" stroke="currentColor" strokeWidth="2"/>
                </svg>
              </div>
            )}
          </div>

          <div className="product-details">
            <span className="product-brand">{producto.marca}</span>
            <h1>{producto.nombre}</h1>

            <div className="product-price-large">{formatPrice(producto.precio)}</div>

            <div className="product-description">
              <h3>Descripción</h3>
              <p>{producto.descripcion}</p>
            </div>

            {producto.caracteristicas && producto.caracteristicas.length > 0 && (
              <div className="product-features-list">
                <h3>Características</h3>
                <ul>
                  {producto.caracteristicas.map((car, index) => (
                    <li key={index}>{car}</li>
                  ))}
                </ul>
              </div>
            )}

            {producto.presentaciones && producto.presentaciones.length > 0 && (
              <div className="presentaciones">
                <h3>Presentación</h3>
                <div className="presentacion-buttons">
                  {producto.presentaciones.map((pres) => (
                    <button
                      key={pres}
                      className={`presentacion-btn ${presentacionSeleccionada === pres ? 'active' : ''}`}
                      onClick={() => setPresentacionSeleccionada(pres)}
                    >
                      {pres}
                    </button>
                  ))}
                </div>
              </div>
            )}

            <div className="add-to-cart-section">
              <div className="quantity-selector">
                <button onClick={() => setCantidad(Math.max(1, cantidad - 1))}>-</button>
                <input
                  type="number"
                  value={cantidad}
                  onChange={(e) => setCantidad(Math.max(1, parseInt(e.target.value) || 1))}
                  min="1"
                />
                <button onClick={() => setCantidad(cantidad + 1)}>+</button>
              </div>

              <button className="add-to-cart-btn" onClick={handleAgregarCarrito}>
                Agregar al Carrito
              </button>
            </div>

            <div className="product-meta">
              <p><strong>Categoría:</strong> {producto.categoria}</p>
              {producto.subcategoria && <p><strong>Subcategoría:</strong> {producto.subcategoria}</p>}
              {producto.uso && <p><strong>Uso:</strong> {producto.uso}</p>}
            </div>
          </div>
        </div>
      </div>

      {showToast && (
        <Toast
          message={`✓ ${producto.nombre} agregado al carrito`}
          type="success"
          onClose={() => setShowToast(false)}
        />
      )}
    </div>
  );
};

export default ProductDetail;
