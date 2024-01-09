<script setup>
defineProps({
})
</script>

<template>
  <!-- Modal -->
  <div class="modal fade" id="updateIncidentModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">Update Incident</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
                <div class="form-group">
                    <label for="shortDescriptionInput">Short description</label>
                    <input v-model="incidentToUpdate.short_description" type="text" class="form-control" id="shortDescriptionInput">
                </div>
                <div class="form-group">
                    <label for="descriptionTextarea">Description</label>
                    <textarea v-model="incidentToUpdate.description" class="form-control" id="descriptionTextarea" rows="3"></textarea>
                </div>
            </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="updateIncident()">Update</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>

<script>
  export default {
    name: "UpdateIncidentModal",
    computed: {
      incidentToUpdate() {
        return this.$store.state.update_incident.incident;
      },
      incidents() {
        return this.$store.state.get_incidents.incidents;
      }
    },
    methods: {
      getIncidents(type) {
        this.$store.dispatch('get_incidents/getIncidents', type);
      },
      async updateIncident() {
        await this.$store.dispatch('update_incident/updateIncident', this.incidentToUpdate);
        this.getIncidents("date");
        this.$emit('close-incident-modal', "update");
      }
    }
  };
</script>