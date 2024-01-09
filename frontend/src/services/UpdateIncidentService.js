import http from "@/http-common";

class UpdateIncidentService {
  update(incident) {
    return http.patch(`/incident/update_incident/${incident.sys_id}`, {
      "description": incident.description,
      "short_description": incident.short_description
    });
  }
}

export default new UpdateIncidentService();