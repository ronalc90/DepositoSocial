import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const productosAPI = {
  getAll: (params) => api.get('/productos/', { params }),
  getById: (id) => api.get(`/productos/${id}/`),
  search: (query) => api.get('/productos/', { params: { search: query } }),
  getByCategoria: (categoria) => api.get('/productos/', { params: { categoria } }),
};

export const categoriasAPI = {
  getAll: () => api.get('/categorias/'),
};

export const pedidosAPI = {
  create: (data) => api.post('/pedidos/', data),
  getById: (id) => api.get(`/pedidos/${id}/`),
  crearPagoEpayco: (data) => api.post('/pago/epayco/', data),
};

export default api;
