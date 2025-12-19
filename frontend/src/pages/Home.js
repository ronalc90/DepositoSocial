import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { productosAPI, categoriasAPI } from '../services/api';
import ProductCard from '../components/ProductCard';
import './Home.css';

const Home = () => {
  const [productos, setProductos] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [productosRes, categoriasRes] = await Promise.all([
          productosAPI.getAll({ activo: true }),
          categoriasAPI.getAll(),
        ]);
        setProductos(productosRes.data.slice(0, 8));
        setCategorias(categoriasRes.data);
      } catch (error) {
        console.error('Error cargando datos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Cargando...</div>;
  }

  return (
    <div className="home">
      <section className="hero">
        <div className="container">
          <h1>Depósito Social - 50 Años de Confianza</h1>
          <p>Herramientas, pinturas, materiales de construcción y más</p>
          <Link to="/categoria/Herramientas Eléctricas" className="cta-button">
            Ver Catálogo Completo
          </Link>
        </div>
      </section>

      <section className="categories">
        <div className="container">
          <h2>Categorías Principales</h2>
          <div className="categories-grid">
            {[
              { name: 'Herramientas Eléctricas', icon: '⚡', slug: 'Herramientas Eléctricas' },
              { name: 'Herramientas Manuales', icon: '🔧', slug: 'Herramientas Manuales' },
              { name: 'Pinturas', icon: '🎨', slug: 'Pinturas y Accesorios' },
              { name: 'Plomería', icon: '🚰', slug: 'Plomería' },
              { name: 'Electricidad', icon: '💡', slug: 'Electricidad' },
              { name: 'Construcción', icon: '🏗️', slug: 'Construcción' },
            ].map((cat) => (
              <Link key={cat.slug} to={`/categoria/${cat.slug}`} className="category-card">
                <span className="category-icon">{cat.icon}</span>
                <h3>{cat.name}</h3>
              </Link>
            ))}
          </div>
        </div>
      </section>

      <section className="featured-products">
        <div className="container">
          <h2>Productos Destacados</h2>
          <div className="products-grid">
            {productos.map((producto) => (
              <ProductCard key={producto._id} producto={producto} />
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
