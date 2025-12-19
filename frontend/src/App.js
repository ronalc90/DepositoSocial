import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CarritoProvider } from './contexts/CarritoContext';
import Header from './components/Header';
import Home from './pages/Home';
import ProductDetail from './pages/ProductDetail';
import Categoria from './pages/Categoria';
import Carrito from './pages/Carrito';
import Checkout from './pages/Checkout';
import ConfirmacionPedido from './pages/ConfirmacionPedido';
import './App.css';

function App() {
  return (
    <CarritoProvider>
      <Router>
        <div className="App">
          <Header />
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/producto/:id" element={<ProductDetail />} />
              <Route path="/categoria/:categoria" element={<Categoria />} />
              <Route path="/carrito" element={<Carrito />} />
              <Route path="/checkout" element={<Checkout />} />
              <Route path="/pedido/confirmacion" element={<ConfirmacionPedido />} />
            </Routes>
          </main>
        </div>
      </Router>
    </CarritoProvider>
  );
}

export default App;
