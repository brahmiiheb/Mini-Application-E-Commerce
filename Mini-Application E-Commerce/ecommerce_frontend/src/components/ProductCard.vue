<template>
    <div class="product-card" :class="{ 'out-of-stock': product.stock === 0 }">
      <!-- Product Image -->
      <div class="product-image">
        <img
          :src="product.image || 'https://via.placeholder.com/150'"
          :alt="product.name"
        />
      </div>
  
      <!-- Product Info -->
      <div class="product-info">
        <h2 class="product-name">{{ product.name }}</h2>
        <p class="product-description">{{ product.description }}</p>
        <p class="product-price">Price: ${{ product.price }}</p>
        <p class="product-stock">
          <span :class="{ 'out-of-stock-label': product.stock === 0 }">
            Stock: {{ product.stock }}
          </span>
          <span v-if="product.stock === 0" class="out-of-stock-notice">
            (Out of Stock)
          </span>
        </p>
      </div>
  
      <!-- Action Buttons -->
      <div class="product-actions">
        <button class="delete-btn" @click="$emit('delete-product', product.id)">
          Delete
        </button>
        <button class="update-btn" @click="$emit('update-stock', product.id)">
          Update Stock
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      product: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  /* General Card Styles */
  .product-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    background-color: #fff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
  }
  
  /* Out of Stock Styling */
  .out-of-stock {
    background-color: #fff6f6;
    border-color: #f5c6cb;
  }
  
  .out-of-stock-label {
    color: #e74c3c;
    font-weight: bold;
  }
  
  .out-of-stock-notice {
    color: #e74c3c;
    font-size: 0.9rem;
    font-weight: bold;
  }
  
  /* Product Image */
  .product-image {
    width: 100%;
    max-width: 200px;
    margin-bottom: 15px;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .product-image img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
  }
  
  /* Product Info */
  .product-info {
    text-align: center;
    margin-bottom: 15px;
  }
  
  .product-name {
    font-size: 1.5rem;
    color: #2c3e50;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .product-description {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 12px;
  }
  
  .product-price {
    font-size: 1rem;
    color: #27ae60;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .product-stock {
    font-size: 0.9rem;
    color: #34495e;
  }
  
  /* Action Buttons */
  .product-actions {
    display: flex;
    gap: 10px;
  }
  
  button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: bold;
    transition: background-color 0.3s;
  }
  
  .delete-btn {
    background-color: #e74c3c;
    color: white;
  }
  
  .delete-btn:hover {
    background-color: #c0392b;
  }
  
  .update-btn {
    background-color: #3498db;
    color: white;
  }
  
  .update-btn:hover {
    background-color: #2980b9;
  }
  </style>
  