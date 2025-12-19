import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useCarrito } from '../contexts/CarritoContext';
import './Header.css';

const Header = () => {
  const { cantidadItems } = useCarrito();
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchTerm.trim()) {
      navigate(`/buscar?q=${encodeURIComponent(searchTerm)}`);
    }
  };

  return (
    <header className="header">
      <div className="header-top">
        <div className="container">
          <Link to="/" className="logo">
            <img
              src="https://depositosocial.com/wp-content/uploads/2024/05/Logo-celebracion-50-anos-deposito-social.png"
              alt="Depósito Social - 50 Años"
              onError={(e) => {
                e.target.onerror = null;
                e.target.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60"><text x="10" y="40" font-family="Arial" font-size="24" font-weight="bold" fill="%23003DA5">Depósito Social</text></svg>';
              }}
            />
          </Link>

          <form className="search-bar" onSubmit={handleSearch}>
            <input
              type="text"
              placeholder="Buscar productos, marcas, categorías..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <button type="submit">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                <path d="M9 17A8 8 0 1 0 9 1a8 8 0 0 0 0 16zM19 19l-4.35-4.35" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
              </svg>
            </button>
          </form>

          <Link to="/carrito" className="cart-button">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="9" cy="21" r="1"/>
              <circle cx="20" cy="21" r="1"/>
              <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
            </svg>
            <span>Carrito</span>
            {cantidadItems() > 0 && <span className="badge">{cantidadItems()}</span>}
          </Link>
        </div>
      </div>

      <nav className="header-nav">
        <div className="container">
          <Link to="/categoria/Herramientas Eléctricas">Herramientas Eléctricas</Link>
          <Link to="/categoria/Herramientas Manuales">Herramientas Manuales</Link>
          <Link to="/categoria/Pinturas y Accesorios">Pinturas</Link>
          <Link to="/categoria/Plomería">Plomería</Link>
          <Link to="/categoria/Electricidad">Electricidad</Link>
          <Link to="/categoria/Construcción">Construcción</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
