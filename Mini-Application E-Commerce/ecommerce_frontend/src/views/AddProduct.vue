<template>
  <div class="add-product-modal">
    <div class="add-product-header">
      <button @click="closeForm" class="close-btn">X</button>
    </div>
    <h1 class="add-product-title">Add New Product</h1>
    <form @submit.prevent="submitForm" class="add-product-form">
      <div class="add-product-group">
        <label for="name">Product Name</label>
        <input
          v-model="newProduct.name"
          id="name"
          placeholder="Enter Product Name"
          required
        />
      </div>
      <div class="add-product-group">
        <label for="description">Description</label>
        <textarea
          v-model="newProduct.description"
          id="description"
          placeholder="Enter Product Description"
          required
        ></textarea>
      </div>
      <div class="add-product-group">
        <label for="price">Price ($)</label>
        <input
          v-model.number="newProduct.price"
          type="number"
          id="price"
          placeholder="Enter Price"
          required
          min="0.00"
        />
      </div>
      <div class="add-product-group">
        <label for="stock">Stock</label>
        <input
          v-model.number="newProduct.stock"
          type="number"
          id="stock"
          placeholder="Enter Stock Quantity"
          required
          min="1"
        />
      </div>
      <button type="submit" class="add-product-submit">Add Product</button>
    </form>

    <!-- Snackbar Notification -->
    <v-snackbar v-model="snackbar.visible" :color="snackbar.color" timeout="6000" >
  {{ snackbar.message }}
</v-snackbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newProduct: {
        name: '',
        description: '',
        price: 0,
        stock: 0,
      },
      snackbar: {             
        visible: false,
        message: '',
        color: '',
      },
    };
  },
  methods: {
    async submitForm() {
      if (this.newProduct.price <= 0) {
        this.showSnackbar('Price must be a positive value.', 'error');
        return;
      }
      if (this.newProduct.stock <= 0) {
        this.showSnackbar('Stock must be a positive number.', 'error');
        return;
      }

      try {
        await this.$store.dispatch('createProduct', this.newProduct);
        this.showSnackbar('Product added successfully!', 'success');
        this.$emit('close');
        this.$router.push('/');
      } catch (error) {
        console.error('Error adding product:', error);
        this.showSnackbar('Failed to add product.', 'error');
      }
    },
    closeForm() {
      this.$emit('close');
    },
    showSnackbar(message, color) {
      this.snackbar.message = message;
      this.snackbar.color = color === 'success' ? 'green' : 'red';
      this.snackbar.visible = true;
    }
  },
};
</script>

<style scoped>
/* Modal Styles */
.add-product-modal {
  max-width: 500px;
  margin: auto;
  position: relative;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.add-product-header {
  position: absolute;
  top: 10px;
  right: 10px;
}

.close-btn {
  background-color: transparent;
  color: #333;
  border: none;
  font-size: 20px;
  cursor: pointer;
  font-weight: bold;
}

.close-btn:hover {
  color: #e74c3c;
}

.add-product-title {
  font-size: 1.8rem;
  color: #3498db;
  text-align: center;
  margin-bottom: 20px;
}

.add-product-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.add-product-group {
  display: flex;
  flex-direction: column;
}

.add-product-group label {
  margin-bottom: 5px;
  font-weight: bold;
  font-size: 0.9rem;
}

.add-product-group input,
.add-product-group textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 0.9rem;
}

.add-product-submit {
  background-color: #2ecc71;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.add-product-submit:hover {
  background-color: #27ae60;
}

/* Snackbar Styles */
.snackbar {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 15px 20px;
  border-radius: 5px;
  color: white;
  font-weight: bold;
  animation: fadeInOut 3s ease forwards;
  z-index: 9999;
}

.snackbar.success {
  background-color: #2ecc71;
}

.snackbar.error {
  background-color: #e74c3c;
}

@keyframes fadeInOut {
  0% {
    opacity: 0;
    transform: translateX(-50%) translateY(10px);
  }
  10%,
  90% {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateX(-50%) translateY(10px);
  }
}
</style>
