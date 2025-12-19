import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useCarrito } from '../contexts/CarritoContext';
import Toast from './Toast';
import './ProductCard.css';

const ProductCard = ({ producto }) => {
  const { agregarItem } = useCarrito();
  const [showToast, setShowToast] = useState(false);

  const formatPrice = (price) => {
    if (!price) return 'Consultar precio';
    return new Intl.NumberFormat('es-CO', {
      style: 'currency',
      currency: 'COP',
      minimumFractionDigits: 0,
    }).format(price);
  };

  const handleAddToCart = (e) => {
    e.preventDefault();
    e.stopPropagation();

    // Agregar al carrito con presentación por defecto si existe
    const presentacion = producto.presentaciones && producto.presentaciones.length > 0
      ? producto.presentaciones[0]
      : '';

    agregarItem(producto, 1, presentacion);
    setShowToast(true);
  };

  return (
    <>
      <div className="product-card">
        <Link to={`/producto/${producto.id || producto._id}`} className="product-card-link">
          <div className="product-image">
            {producto.imagen ? (
              <img src={producto.imagen} alt={producto.nombre} />
            ) : (
              <div className="no-image">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none">
                  <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" strokeWidth="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5" fill="currentColor"/>
                  <path d="M21 15l-5-5L5 21" stroke="currentColor" strokeWidth="2"/>
                </svg>
              </div>
            )}
          </div>

          <div className="product-info">
            <span className="product-brand">{producto.marca}</span>
            <h3 className="product-name">{producto.nombre}</h3>

            {producto.caracteristicas && producto.caracteristicas.length > 0 && (
              <p className="product-features">
                {producto.caracteristicas.slice(0, 2).join(' • ')}
              </p>
            )}

            <div className="product-footer">
              <span className="product-price">{formatPrice(producto.precio)}</span>
              {producto.presentaciones && producto.presentaciones.length > 0 && (
                <span className="product-presentations">
                  {producto.presentaciones.length} presentaciones
                </span>
              )}
            </div>
          </div>
        </Link>

        <button
          className="add-to-cart-card-btn"
          onClick={handleAddToCart}
          title="Agregar al carrito"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="9" cy="21" r="1"/>
            <circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>
          <span>Agregar</span>
        </button>
      </div>

      {showToast && (
        <Toast
          message={`✓ ${producto.nombre} agregado al carrito`}
          type="success"
          onClose={() => setShowToast(false)}
        />
      )}
    </>
  );
};

export default ProductCard;
