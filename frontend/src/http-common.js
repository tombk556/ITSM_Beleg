import axios from "axios";

export default axios.create({
  baseURL: "https://fastapibackend.azurewebsites.net",
  headers: {
    "Content-type": "application/json"
  }
});