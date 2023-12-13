<script setup>
  defineProps({
  })
</script>

<template>
  <div class="input-group">
      <input
        type="text"
        class="form-control"
        placeholder="Incident Number"
        v-model="selectedNumber"
        @keyup.enter="getIncidentByNumber(selectedNumber)"
      />
      <button class="btn btn-outline-secondary" @click="getIncidentByNumber(selectedNumber)">
        <i class="bi bi-search"></i> 
      </button>
    </div>
</template>

<style scoped>
</style>

<script>
  export default {
    name: "FilterByNumber",
    data() {
      return {
        selectedNumber: null
      }
    },
    methods: {
      getIncidentByNumber(number) {
        this.$store.dispatch('incidents/getIncidentByNumber', number);
      }
    }
  };
</script>
