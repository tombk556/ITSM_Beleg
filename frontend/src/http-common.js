import axios from "axios";

export default axios.create({
  baseURL: "http://20.93.41.21:8000",
  headers: {
    "Content-type": "application/json"
  }
});