import GetIncidentsService from "@/services/GetIncidentsService";
import GetIncidentsByStateService from "@/services/GetIncidentsByStateService";

export default {
  namespaced: true,
  state: {
    incidents: []
  },
  mutations: {
    setIncidents(state, incidents) {
      state.incidents = incidents;
    }
  },
  actions: {
    async getIncidents({ commit }, type) {
      try {
        const response = await GetIncidentsService.getAll(type);
        commit('setIncidents', response.data);
      } catch (error) {
        console.error(error);
        // Optionally handle errors here
      }
    },
    async getIncidentsByState({ commit, dispatch }, stateId) {
      console.log(stateId)
      // If state = All
      if (stateId == 0) {
        // Call the getIncidents action with a default type, for example, "date"
        dispatch('getIncidents', 'date');
      } else {
          try {
            const response = await GetIncidentsByStateService.getAll(stateId);
            commit('setIncidents', response.data);
          } catch (error) {
            console.error(error);
            // Optionally handle errors here
          }
      }
    }
  }
}