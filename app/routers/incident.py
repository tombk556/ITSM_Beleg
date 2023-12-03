from fastapi import APIRouter, status
from ..config import config
from .. import schemas
import requests

incident = APIRouter(
    prefix="/incident",
    tags=['Incident'])

INSTANCE = config.get("INSTANCE_SN")
USERNAME_SN = config.get("USERNAME_SN")
PASSWORD_SN = config.get("PASSWORD_SN")

@incident.get("/get_incident/{type}", status_code=status.HTTP_200_OK)
def get_incidents(type: str = None):
    incidents = _incidents(INSTANCE, USERNAME_SN, PASSWORD_SN)
    
    if type == "date":
        return sorted(incidents, key=lambda x: x["date"], reverse=True)
    elif type == "number":
        return sorted(incidents, key=lambda x: x["number"], reverse=True) 
    elif type == "state":
        return sorted(incidents, key=lambda x: x["state"], reverse=False) 
    else:
        return incidents


@incident.post("/create_incident", status_code=status.HTTP_201_CREATED, response_model=schemas.Incident)
def create_incident(inc: schemas.CreateIncident):
    return {
        "short_description": inc.short_description,
        "description" : inc.description
    }

def _incidents(instance, user, pwd):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    url = f"https://{instance}.lab.service-now.com/api/now/table/incident"
    try:
        response = requests.get(url, auth=(user, pwd), headers=headers)

        if response.status_code != 200:
            return {
                "Status": response.status_code,
                "Error Response": response.json()
            }
        else:
            return incident_data(data=response.json())

    except Exception as error:
        return {
            "Status": "Intenal Server Error",
            "Error Response": error
        }
        
def incident_data(data):
    incidents = []
    
    for result_item in data["result"]:
        incident = {
            "number" : result_item.get("number"),
            "date" : result_item.get("sys_updated_on"),
            "short_description" : result_item.get("short_description"),
            "description" : result_item.get("description"),
            "state" : result_item.get("incident_state")
        }
        
        incidents.append(incident)
    
    return incidents