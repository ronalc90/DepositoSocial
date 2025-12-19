import React, { useEffect, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import './ConfirmacionPedido.css';

const ConfirmacionPedido = () => {
  const [searchParams] = useSearchParams();
  const pedidoId = searchParams.get('pedido');
  const [countdown, setCountdown] = useState(5);

  useEffect(() => {
    if (countdown > 0) {
      const timer = setTimeout(() => setCountdown(countdown - 1), 1000);
      return () => clearTimeout(timer);
    }
  }, [countdown]);

  return (
    <div className="confirmacion-pedido">
      <div className="container">
        <div className="confirmacion-card">
          <div className="success-icon">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="10" fill="#FFC800" />
              <path
                d="M9 12l2 2 4-4"
                stroke="#003DA5"
                strokeWidth="3"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </div>

          <h1>¡Pedido Realizado con Éxito!</h1>

          <div className="pedido-info">
            <p className="pedido-numero">
              Número de Pedido: <strong>#{pedidoId}</strong>
            </p>
            <p className="pedido-mensaje">
              Hemos recibido tu pedido y lo procesaremos a la brevedad.
            </p>
          </div>

          <div className="info-box">
            <h3>¿Qué sigue?</h3>
            <ul>
              <li>📧 Recibirás un correo de confirmación con los detalles</li>
              <li>📦 Prepararemos tu pedido</li>
              <li>🚚 Te notificaremos cuando esté listo para entrega</li>
            </ul>
          </div>

          <div className="nota-pago">
            <p>
              <strong>Nota:</strong> En producción, aquí se procesaría el pago real con ePayco PSE.
              <br />
              Esta es una demostración del flujo completo del e-commerce.
            </p>
          </div>

          <div className="acciones">
            <Link to="/" className="btn-primary">
              Volver al Inicio
            </Link>
            <Link to={`/categoria/Herramientas Eléctricas`} className="btn-secondary">
              Seguir Comprando
            </Link>
          </div>

          {countdown > 0 && (
            <p className="redirect-mensaje">
              Redirigiendo a inicio en {countdown} segundos...
            </p>
          )}
          {countdown === 0 && window.location.replace('/')}
        </div>
      </div>
    </div>
  );
};

export default ConfirmacionPedido;
