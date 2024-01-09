import CreateIncidentService from "@/services/CreateIncidentService";

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
    async createIncident({ commit }, incident) {
      try {
        const response = await CreateIncidentService.create(incident);
        commit('setIncident', response.data);
      } catch (error) {
        console.error(error);
        // Optionally handle errors here
      }
    }
  }
}