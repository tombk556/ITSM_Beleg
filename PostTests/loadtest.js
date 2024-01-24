import http from 'k6/http'
import { sleep } from 'k6'

let remoteip = "4.207.199.248:8000"; // Ziel ip und port
//let remoteip = "127.0.0.1:8000"; // Ziel ip und port

//definition der (Abbruch-)Bediengungen
export let options = {
    vus: 3,             // virtual user - emulate number of user
    duration: '30s',    // run test for given time
    thresholds: {
        http_req_duration: ["p(95)<8000"] // für Gitlab-Runner hoch gesetzt
        //http_req_duration: ["p(95)<200"] // lokal
    }
};

//eigentliche Testfall
export default function(){
    var res =   http.get(`http://${remoteip}/incident/get_incidents/date`); //alle incidents (sortiert noch Datum)
    console.log("Response time was "+ String(res.timings.duration)+ " ms");
    sleep(1);
}
