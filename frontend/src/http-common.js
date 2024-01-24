import axios from "axios";

export default axios.create({
  baseURL: "http://fastapi-app-service.itsmbeleg.svc.cluster.local:8000",
  headers: {
    "Content-type": "application/json"
  }
});
