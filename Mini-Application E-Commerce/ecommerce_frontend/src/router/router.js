// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/HomePage.vue'; 
import AddProduct from '@/views/AddProduct.vue';  

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/add-product',
    name: 'AddProduct',
    component: AddProduct,
  },
  // Add other routes here as necessary
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
