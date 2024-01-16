import http from "@/http-common";

class GetIncidentByNumberService {
  get(number) {
    return http.get(`/incident/get_incident_by_number/${number}`);
  }
}

export default new GetIncidentByNumberService();