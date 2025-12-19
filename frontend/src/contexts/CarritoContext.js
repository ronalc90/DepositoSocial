import React, { createContext, useContext, useState, useEffect } from 'react';

const CarritoContext = createContext();

export const useCarrito = () => {
  const context = useContext(CarritoContext);
  if (!context) {
    throw new Error('useCarrito debe usarse dentro de CarritoProvider');
  }
  return context;
};

export const CarritoProvider = ({ children }) => {
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem('carrito');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem('carrito', JSON.stringify(items));
  }, [items]);

  const agregarItem = (producto, cantidad = 1, presentacion = '') => {
    setItems((prevItems) => {
      const existingIndex = prevItems.findIndex(
        (item) => (item.producto.id || item.producto._id) === (producto.id || producto._id) && item.presentacion === presentacion
      );

      if (existingIndex >= 0) {
        const newItems = [...prevItems];
        newItems[existingIndex].cantidad += cantidad;
        return newItems;
      }

      return [...prevItems, { producto, cantidad, presentacion }];
    });
  };

  const actualizarCantidad = (index, cantidad) => {
    if (cantidad <= 0) {
      eliminarItem(index);
      return;
    }

    setItems((prevItems) => {
      const newItems = [...prevItems];
      newItems[index].cantidad = cantidad;
      return newItems;
    });
  };

  const eliminarItem = (index) => {
    setItems((prevItems) => prevItems.filter((_, i) => i !== index));
  };

  const limpiarCarrito = () => {
    setItems([]);
  };

  const calcularTotal = () => {
    return items.reduce((total, item) => {
      const precio = parseFloat(item.producto.precio || 0);
      return total + precio * item.cantidad;
    }, 0);
  };

  const cantidadItems = () => {
    return items.reduce((total, item) => total + item.cantidad, 0);
  };

  const value = {
    items,
    agregarItem,
    actualizarCantidad,
    eliminarItem,
    limpiarCarrito,
    calcularTotal,
    cantidadItems,
  };

  return <CarritoContext.Provider value={value}>{children}</CarritoContext.Provider>;
};
