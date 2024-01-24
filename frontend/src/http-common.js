import axios from "axios";

export default axios.create({
  baseURL: "http://4.208.76.0:8000",
  headers: {
    "Content-type": "application/json"
  }
});