import http from "@/http-common";

class CreateIncidentsService {
  create(incident) {
    return http.post(`/incident/create_incident`, {
      "description": incident.description,
      "short_description": incident.short_description
    });
  }
}

export default new CreateIncidentsService();