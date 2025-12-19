import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { productosAPI } from '../services/api';
import ProductCard from '../components/ProductCard';
import './Categoria.css';

const Categoria = () => {
  const { categoria } = useParams();
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProductos = async () => {
      setLoading(true);
      try {
        const response = await productosAPI.getByCategoria(
          categoria.charAt(0).toUpperCase() + categoria.slice(1)
        );
        setProductos(response.data);
      } catch (error) {
        console.error('Error cargando productos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProductos();
  }, [categoria]);

  if (loading) {
    return <div className="loading">Cargando...</div>;
  }

  return (
    <div className="categoria-page">
      <div className="container">
        <h1>{categoria.charAt(0).toUpperCase() + categoria.slice(1)}</h1>
        <p className="categoria-count">{productos.length} productos encontrados</p>

        {productos.length === 0 ? (
          <div className="no-productos">
            <p>No se encontraron productos en esta categoría</p>
          </div>
        ) : (
          <div className="products-grid">
            {productos.map((producto) => (
              <ProductCard key={producto._id} producto={producto} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Categoria;
