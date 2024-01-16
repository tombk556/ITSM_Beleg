import UpdateIncidentService from "@/services/UpdateIncidentService";

export default {
  namespaced: true,
  state: {
    incident: {}
  },
  mutations: {
    setIncident(state, incident) {
      state.incident = incident;
    }
  },
  actions: {
    async updateIncident({ commit }, incident) {
      try {
        const response = await UpdateIncidentService.update(incident);
        commit('setIncident', response.data);
      } catch (error) {
        console.error(error);
        // Optionally handle errors here
      }
    }
  }
}