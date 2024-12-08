<template>
  <div class="pagination">
    <button
      :disabled="currentPage === 1"
      @click="$emit('changePage', currentPage - 1)"
    >
      Previous
    </button>
    <span class="page-info">
      Page {{ currentPage }} of {{ totalPages }}
    </span>
    <button
      :disabled="currentPage === totalPages"
      @click="$emit('changePage', currentPage + 1)"
    >
      Next
    </button>
  </div>
</template>

<script>
export default {
  props: {
    currentPage: {
      type: Number,
      required: true,
    },
    totalPages: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center; 
  gap: 10px;
  margin-top: 20px;
}

.page-info {
  font-weight: bold; 
}

button {
  padding: 8px 12px; 
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out; 
}

button:hover {
  background-color: #388e3c; 
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  opacity: 0.7; 
}
</style>