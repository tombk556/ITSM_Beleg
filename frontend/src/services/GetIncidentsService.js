import http from "@/http-common";

class GetIncidentsService {
  getAll(type) {
    return http.get(`/incident/get_incidents/${type}`);
  }
}

export default new GetIncidentsService();