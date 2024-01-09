import http from "@/http-common";

class DeleteIncidentsService {
  delete(sysId) {
    return http.delete(`/incident/delete_incident/${sysId}`);
  }
}

export default new DeleteIncidentsService();