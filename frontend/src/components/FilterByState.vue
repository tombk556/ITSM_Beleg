<script setup>
  defineProps({
  })
</script>

<template>
  <select class="form-select" v-model="selectedOption" @change="getIncidentsByState(selectedOption)">
      <option v-for="(option, index) in options" :key="index" :value="option.value">
          {{ option.label }}
      </option>
  </select>
</template>

<style scoped>
</style>

<script>
  export default {
    name: "FilterByState",
    data() {
      return {
        selectedOption: '0', // set the default value to 'All'
        options: [
            { value: '0', label: 'All' },
            { value: '1', label: 'New' },
            { value: '2', label: 'In Progress' },
            { value: '3', label: 'On Hold' },
            { value: '6', label: 'Resolved' },
            { value: '7', label: 'Closed' },
            { value: '8', label: 'Canceled' },
        ]
      };
    },
    methods: {
      getIncidentsByState(stateId) {
        this.$store.dispatch('get_incidents/getIncidentsByState', stateId);
      }
    }
  };
</script>
