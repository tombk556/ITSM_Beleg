import axios from "axios";

export default axios.create({
  baseURL: "https://itsmgruppe1backend.azurewebsites.net",
  headers: {
    "Content-type": "application/json"
  }
});