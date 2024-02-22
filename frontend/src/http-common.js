import axios from "axios";

export default axios.create({
  baseURL: "http://4.231.134.197:8000",
  headers: {
    "Content-type": "application/json"
  }
});
