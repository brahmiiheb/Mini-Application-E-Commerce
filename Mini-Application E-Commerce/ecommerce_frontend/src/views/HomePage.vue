<template>
  <div class="home">
    <!-- Page Header -->
    <header class="home-header">
      <h1 class="title">Product Inventory</h1>
      <p class="subtitle">Easily manage and track your products</p>
    </header>

    <!-- Filter and Add Product Button -->
    <div class="filters">
      <button class="filter-btn" @click="toggleInStockFilter">
        {{ filterInStock ? 'Show All Products' : 'Show In-Stock Only' }}
      </button>
      <font-awesome-icon @click="openStatsModal" class="admin-btn" icon="fa-solid fa-chart-bar" />
      <button @click="openAddProductModal" class="add-product-btn">+ Add Product</button>
    </div>

    <!-- Product Cards -->
    <div class="product-list">
      <ProductCard
        v-for="product in displayedProducts"
        :key="product.id"
        :product="product"
        @delete-product="openDeleteDialog"
        @update-stock="handleUpdateStock"
      />
    </div>

    <!-- Add Product Modal -->
    <v-dialog v-model="isAddProductModalOpen" max-width="600px">
      <AddProduct @close="closeAddProductModal" />
    </v-dialog>

    <!-- Statistics Modal -->
    <v-dialog v-model="isStatsModalOpen" max-width="450px">
  <v-card class="stats-modal">
    <v-card-title class="stats-title">Product Statistics</v-card-title>
    <v-card-text class="stats-content">
      <p><span>Total Products:</span> <strong>{{ totalProducts }}</strong></p>
      <p><span style="color: green;">In Stock:</span> <strong>{{ inStockCount }}</strong></p>
      <p><span style="color: red;">Out of Stock:</span> <strong style="color: red;">{{ outOfStockCount }}</strong></p>
    </v-card-text>
    <v-card-actions>
      <v-btn class="close-btn" @click="closeStatsModal">Close</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>



    <!-- Pagination -->
    <div v-if="totalPages > 1" class="pagination-container">
      <Pagination
        :currentPage="currentPage"
        :totalPages="totalPages"
        @changePage="changePage"
      />
    </div>

    <!-- Confirmation Delete Modal -->
    <ConfirmDeleteModal 
      ref="deleteModal" 
      :isDialogOpen="isModalVisible" 
      @update:isDialogOpen="isModalVisible = $event"
      @deleted="handleDeleted" 
      :productId="productToDelete"
      @close="closeDeleteDialog"
    />

    <!-- Snackbar Notifications -->
<v-snackbar v-model="snackbar.visible" :color="snackbar.color" timeout="3000" >
  {{ snackbar.message }}
</v-snackbar>

  </div>
</template>

<script>
import { mapState } from 'vuex';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'; // Import FontAwesome
import ProductCard from '@/components/ProductCard.vue';
import Pagination from '@/components/Pagi-nation.vue';
import ConfirmDeleteModal from '@/components/ConfirmDeleteModal.vue';
import AddProduct from '@/views/AddProduct.vue';

export default {
  components: { ProductCard, Pagination, ConfirmDeleteModal, AddProduct, FontAwesomeIcon },
  data() {
    return {
      isModalVisible: false,  // Confirmation delete modal visibility
      productToDelete: null, // ID of the product to delete
      isAddProductModalOpen: false, // Add product modal visibility
      isStatsModalOpen: false, // Stats modal visibility
      snackbar: {             // Snackbar state for notifications
        visible: false,
        message: '',
        color: '',
      },
    };
  },
  computed: {
    ...mapState([
      'displayedProducts',
      'currentPage',
      'totalProducts',
      'productsPerPage',
      'filterInStock',
    ]),
    totalPages() {
      return Math.ceil(this.totalProducts / this.productsPerPage);
    },
    inStockCount() {
      return this.totalProducts - this.outOfStockCount; // Fix the calculation
    },
    outOfStockCount() {
      return this.displayedProducts.filter(product => product.stock === 0).length;
    }
  },
  methods: {
    toggleInStockFilter() {
      this.$store.commit('TOGGLE_IN_STOCK_FILTER');
      this.$store.dispatch('fetchProducts');
    },
    changePage(page) {
      this.$store.dispatch('changePage', page);
    },
    openDeleteDialog(productId) {
      this.productToDelete = productId;
      this.isModalVisible = true;
    },
    closeDeleteDialog() {
      this.isModalVisible = false;
    },
    handleUpdateStock(productId) {
      const newStock = prompt('Enter new stock value:');

      if (newStock !== null) {
        this.$store
          .dispatch('updateProduct', { id: productId, updates: { stock: newStock } })
          .then(() => {
            this.$store.dispatch('fetchProducts');
            this.showSnackbar('Stock updated successfully!', 'success');
          })
          .catch(() => {
            this.showSnackbar('Failed to update stock.', 'error');
          });
      }
    },
    async handleDeleted() {
      console.log('Product deleted');
      await this.$store.dispatch('fetchProducts');
      this.closeDeleteDialog();
      this.showSnackbar('Product deleted successfully!', 'success');
    },
    openAddProductModal() {
      this.isAddProductModalOpen = true;
    },
    closeAddProductModal() {
      this.isAddProductModalOpen = false;
    },
    openStatsModal() {
      this.isStatsModalOpen = true;
    },
    closeStatsModal() {
      this.isStatsModalOpen = false;
    },
    showSnackbar(message, color) {
      this.snackbar.message = message;
      this.snackbar.color = color === 'success' ? 'green' : 'red';
      this.snackbar.visible = true;
    }
  },
  created() {
    this.$store.dispatch('fetchProducts');
  },
};
</script>

<style scoped>
/* General Styles */
.home {
  padding: 20px;
  background-color: #f9fafb;
  color: #333;
  font-family: 'Arial', sans-serif;
}

/* Header Section */
.home-header {
  text-align: center;
  margin-bottom: 30px;
}

.title {
  font-size: 2.5rem;
  color: #2c3e50;
  font-weight: bold;
}

.subtitle {
  font-size: 1rem;
  color: #7f8c8d;
  margin-top: 5px;
}

/* Filter and Add Product Section */
.filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.filter-btn {
  background-color: #3498db;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.filter-btn:hover {
  background-color: #2980b9;
}

.add-product-btn {
  background-color: #2ecc71;
  color: white;
  padding: 10px 15px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.add-product-btn:hover {
  background-color: #27ae60;
}

.admin-btn {
  color: #f39c12;
  font-size: 1.5rem;
  cursor: pointer;
}

.admin-btn:hover {
  color: #e67e22;
}

/* Product Cards Section */
.product-list {
  display: grid;
  justify-items: center;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 50px;
  margin-bottom: 30px;
}

/* Pagination */
.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

/* Add Product Modal Styling */
.add-product-modal-overlay,
.stats-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.add-product-modal,
.stats-modal {
  background-color: #fff;
  padding: 30px;
  border-radius: 10px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}

.close-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 5px 10px;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.close-btn:hover {
  background-color: #c0392b;
}
/* General Modal Overlay */
.stats-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7); /* Darker overlay for better contrast */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  transition: opacity 0.3s ease-in-out;
}

/* Modal Styling */
.stats-modal {
  background-color: #ffffff;
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  animation: fadeIn 0.5s ease-out;
}

/* Modal Title */
.stats-title {
  font-size: 1.75rem;
  color: #2c3e50;
  font-weight: 600;
  text-align: center;
  margin-bottom: 20px;
}

/* Statistics Content */
.stats-content {
  font-size: 1rem;
  color: #7f8c8d;
  margin-bottom: 20px;
}

.stats-content p {
  margin: 10px 0;
  line-height: 1.5;
}

/* Close Button */
.close-btn {
  background-color: #e74c3c;
  color: white;
  padding: 10px 20px;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s ease;
  display: block;
  margin: 0 auto;
}

.close-btn:hover {
  background-color: #c0392b;
}

/* Animation for Fade-In Effect */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Updated Modal Overlay */
.stats-modal-overlay {
  backdrop-filter: blur(5px);
  background-color: rgba(0, 0, 0, 0.6); /* Glassmorphism effect */
}

/* Updated Modal Card */
.stats-modal {
  background: linear-gradient(135deg, #ffffff 70%, #f9f9f9);
  border-radius: 12px;
  padding: 25px;
  max-width: 450px;
  box-shadow: 0px 15px 30px rgba(0, 0, 0, 0.2); /* Elevated shadow for depth */
}

/* Title */
.stats-title {
  font-size: 1.8rem;
  color: #34495e;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
  border-bottom: 2px solid #ecf0f1;
  padding-bottom: 10px;
}

/* Statistics Content */
.stats-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.stats-content p {
  display: flex;
  justify-content: space-between;
  font-size: 1.1rem;
  font-weight: 500;
  color: #7f8c8d;
}

.stats-content strong {
  color: #2ecc71;
}

/* Close Button */
.close-btn {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  color: #ffffff;
  font-size: 1rem;
  padding: 10px;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  text-transform: uppercase;
  transition: transform 0.3s ease, background 0.3s ease;
}

.close-btn:hover {
  background: linear-gradient(135deg, #c0392b, #e74c3c);
  transform: translateY(-3px);
}


</style>
