import http from "@/http-common";

class GetIncidentsSinceYesterdayService {
  getAll() {
    return http.get(`/incident/get_incidents_since/yesterday`);
  }
}

export default new GetIncidentsSinceYesterdayService();