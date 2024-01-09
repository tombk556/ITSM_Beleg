import http from "@/http-common";

class GetIncidentsByStateService {
  getAll(stateId) {
    return http.get(`/incident/get_incidents_by_state/${stateId}`);
  }
}

export default new GetIncidentsByStateService();