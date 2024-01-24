import axios from "axios";

export default axios.create({
  baseURL: "http://4.207.199.248:8000",
  headers: {
    "Content-type": "application/json"
  }
});
