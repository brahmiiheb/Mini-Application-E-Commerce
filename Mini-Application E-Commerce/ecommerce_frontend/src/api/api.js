import axios from 'axios';

// Axios instance
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Replace with your actual backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// CRUD functions for products
export const fetchProducts = (params) => apiClient.get('/products', { params }); // Supports pagination/filtering
export const addProduct = (product) => apiClient.post('/products', product);
export const updateProduct = (id, updates) => apiClient.patch(`/products/${id}`, updates);
export const deleteProduct = (id) => apiClient.delete(`/products/${id}`);
