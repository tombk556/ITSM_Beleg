import http from 'k6/http'
import { Counter } from 'k6/metrics'    
import { check as loadTestingCheck, sleep } from 'k6'

let failedTestCases = new Counter('failedTestCases');  // (mit "Erwartung", dass es 0 bleibt)
let remoteip = "127.0.0.1:8000"

export let options = {
    thresholds: {
      failedTestCases: [{ threshold: 'count==0'}],
    },
    iterations: 1,
    //vus: 1, // for "k6 cloud"-Testing
    //duration: "30s"
}

let check = function (obj, conditionArray, tags) {
  let result = loadTestingCheck(obj, conditionArray, tags || {});
  failedTestCases.add(!result);
  return result;
}

export default function (){
  var res =   http.get(`http://${remoteip}/incident/get_incidents/date`); //alle incidents (sortiert noch Datum)

  // Check 1 - HTTP Statuscode korrekt
  check(res.status, {
    "API is working": (status) => status === 200
  });

  // Check 1- Content entspricht der Erwartung
  let jsonData = res.json();
  // Option 1a - mindestens eine Ausgabe
  check(jsonData, {
    "API response has at least one incident": (jsonData) => Array.isArray(jsonData) && jsonData.length > 0
  });

  // Option 1b - Der erste Eintrag enthält die gewollten keys
  check(jsonData[0], {
    "First incident contains required keys": (firstIncident) =>
      firstIncident.hasOwnProperty("sys_id") &&
      firstIncident.hasOwnProperty("number") &&
      firstIncident.hasOwnProperty("date") &&
      firstIncident.hasOwnProperty("short_description") &&
      firstIncident.hasOwnProperty("description") &&
      firstIncident.hasOwnProperty("state")
  }); 
}