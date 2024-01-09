import DeleteIncidentService from "@/services/DeleteIncidentService";

export default {
  namespaced: true,
  state: {
    incident: {}
  },
  actions: {
    async deleteIncident({}, sysId) {
      try {
        await DeleteIncidentService.delete(sysId);
      } catch (error) {
        console.error(error);
        // Optionally handle errors here
      }
    }
  }
}