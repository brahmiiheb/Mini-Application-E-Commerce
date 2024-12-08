<template>
    <div v-if="isDialogOpen" class="modal-overlay" @click.self="cancelDelete">
      <div class="modal-content">
        <h3>Confirm Delete</h3>
        <p>Are you sure you want to delete this product? This action cannot be undone.</p>
        <div class="modal-actions">
          <button @click="cancelDelete">Cancel</button>
          <button class="delete-btn" @click="confirmDelete">Delete</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isDialogOpen: {
        type: Boolean,
        required: true,
      },
      productId: {
        type: Number,
        required: true, // Ensure productId is passed as a prop
      },
    },
    methods: {
      updateDialogState(value) {
        // Emit the update to the parent component
        this.$emit('update:isDialogOpen', value);
      },
      cancelDelete() {
        this.$emit('update:isDialogOpen', false);  // Close the dialog on cancel
      },
      async confirmDelete() {
        if (this.productId) {
          try {
            await this.$store.dispatch("deleteProduct", this.productId); // Pass the correct product ID
            this.$emit("deleted"); // Emit event to notify parent that the product has been deleted
            this.$emit('update:isDialogOpen', false); // Close the dialog after deletion
          } catch (error) {
            console.error("Error deleting product:", error);
            this.$emit('update:isDialogOpen', false); // Close dialog if error occurs
          }
        } else {
          console.error("Product ID is missing");
          this.$emit('update:isDialogOpen', false);
        }
      },
    },
  };
  </script>
  
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
    max-width: 100%;
  }
  
  .modal-actions {
    margin-top: 20px;
    display: flex;
    justify-content: flex-end;
  }
  
  button {
    padding: 10px 20px;
    margin: 0 5px;
    cursor: pointer;
    border: none;
    border-radius: 5px;
  }
  
  button.delete-btn {
    background-color: red;
    color: white;
  }
  
  button:hover {
    opacity: 0.8;
  }
  </style>
  