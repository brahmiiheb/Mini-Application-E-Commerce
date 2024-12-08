import { createStore } from 'vuex';
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/products/';

const store = createStore({
  state: {
    products: [],
    displayedProducts: [],
    currentPage: 1,
    totalProducts: 0,
    productsPerPage: 5,
    filterInStock: false,
  },
  mutations: {
    SET_PRODUCTS(state, products) {
      state.products = products;
      state.totalProducts = products.length;
    },
    SET_DISPLAYED_PRODUCTS(state, products) {
      state.displayedProducts = products;
    },
    SET_CURRENT_PAGE(state, page) {
      state.currentPage = page;
    },
    TOGGLE_IN_STOCK_FILTER(state) {
      state.filterInStock = !state.filterInStock;
    },
    ADD_PRODUCT(state, product) {
      state.products.unshift(product); // Add the new product to the start of the array
      state.totalProducts++;
    },
    DELETE_PRODUCT(state, productId) {
      state.products = state.products.filter(product => product.id !== productId);
      state.totalProducts--;
    },
    UPDATE_PRODUCT(state, updatedProduct) {
      const index = state.products.findIndex(product => product.id === updatedProduct.id);
      if (index !== -1) {
        state.products.splice(index, 1, updatedProduct);
      }
    },
  },
  actions: {
    async fetchProducts({ commit, state, dispatch }) {
      try {
        const filterQuery = state.filterInStock ? '?in_stock=true' : '';
        const response = await axios.get(`${API_BASE_URL}${filterQuery}`);
        commit('SET_PRODUCTS', response.data);
        dispatch('applyPagination');
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
    async createProduct({ commit }, newProduct) {
      try {
        const response = await axios.post(`${API_BASE_URL}create/`, newProduct);
        commit('ADD_PRODUCT', response.data);
      } catch (error) {
        console.error('Error creating product:', error);
      }
    },
    async deleteProduct({ commit }, productId) {
      try {
        await axios.delete(`${API_BASE_URL}${productId}/delete/`);
        commit('DELETE_PRODUCT', productId);
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    },
    async updateProduct({ commit }, { id, updates }) {
      try {
        const response = await axios.put(`${API_BASE_URL}${id}/update/`, updates);
        commit('UPDATE_PRODUCT', response.data);
      } catch (error) {
        console.error('Error updating product:', error);
      }
    },
    applyPagination({ commit, state }) {
      const startIndex = (state.currentPage - 1) * state.productsPerPage;
      const endIndex = startIndex + state.productsPerPage;
      const paginatedProducts = state.products.slice(startIndex, endIndex);
      commit('SET_DISPLAYED_PRODUCTS', paginatedProducts);
    },
    changePage({ commit, dispatch }, page) {
      commit('SET_CURRENT_PAGE', page);
      dispatch('applyPagination');
    },
  },
});

export default store;
