<script setup>
defineProps({
})
</script>

<template>
  <!-- Modal -->
  <div class="modal fade" id="deleteIncidentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">Delete Incident</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>Are you sure you want to delete the incident {{incidentToDelete.number}} ?</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="deleteIncident()">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>

<script>
  export default {
    name: "DeleteIncidentModal",
    computed: {
      incidentToDelete() {
        return this.$store.state.delete_incident.incident;
      },
      incidents() {
        return this.$store.state.get_incidents.incidents;
      }
    },
    methods: {
      getIncidents(type) {
        this.$store.dispatch('get_incidents/getIncidents', type);
      },
      async deleteIncident() {
        await this.$store.dispatch('delete_incident/deleteIncident', this.incidentToDelete.sys_id);
        this.getIncidents("date");
        this.$emit('close-incident-modal', "delete");
      }
    }
  };
</script>