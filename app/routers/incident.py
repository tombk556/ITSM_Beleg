from fastapi import APIRouter, status, HTTPException
from ..config import settings
from .. import schemas
import requests

incident = APIRouter(
    prefix="/incident",
    tags=['Incident'])

INSTANCE = settings.instancesn
USERNAME_SN = settings.usernamesn
PASSWORD_SN = settings.passwordsn


# GET-Methoden zur Abrufung der Incidents

@incident.get("/get_incidents/{type}", status_code=status.HTTP_200_OK)
def get_incidents(type):
    incidents = _get_all_incidents(INSTANCE, USERNAME_SN, PASSWORD_SN)

    if type == "date":
        return sorted(incidents, key=lambda x: x["date"], reverse=True)
    elif type == "number":
        return sorted(incidents, key=lambda x: x["number"], reverse=True)
    elif type == "state":
        return sorted(incidents, key=lambda x: x["state"], reverse=True)
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Onyl choose between date, number or state filter")


@incident.get("/get_incident_by_number/{number}")
def get_incident_by_number(number: str):
    return _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="number", filter_element=number)


@incident.get("/get_incidents_by_state/{state}")
def get_incidents_by_state(state: int):
    return _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="incident_state", filter_element=state)


def _get_all_incidents(instance, user, pwd):
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
    return

def _get_incident(instance, user, pwd, filter, filter_element, with_sys_id = False):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    if filter == "number":
        url = f"https://{instance}.lab.service-now.com/api/now/table/incident?{filter}={filter_element}"
    else:
        url = f"https://{instance}.lab.service-now.com/api/now/table/incident?incident_state={filter_element}"
        
    try:
        response = requests.get(url, auth=(user, pwd), headers=headers)

        if response.status_code != 200:
            return {
                "Status": response.status_code,
                "Error Response": response.json()
            }
        else:
            return incident_data(response.json(), with_sys_id)

    except Exception as error:
        return {
            "Status": "Intenal Server Error",
            "Error Response": error
        }

def incident_data(data, with_sys_id = False):
    incidents = []

    for result_item in data["result"]:
        incident = {
            "number": result_item.get("number"),
            "date": result_item.get("sys_updated_on"),
            "short_description": result_item.get("short_description"),
            "description": result_item.get("description"),
            "state": result_item.get("incident_state")
        }
        if with_sys_id:
            incident.update({"sys_id": result_item.get("sys_id")})
        
        incidents.append(incident)

    return incidents


# POST-Methode zur Erstellung neuer Incidents

@incident.post("/create_incident", status_code=status.HTTP_201_CREATED, response_model=schemas.Incident)
def create_incident(inc: schemas.CreateIncident):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"
            }
    url = f"https://{INSTANCE}.lab.service-now.com/api/now/table/incident"
    
    incident_data = {
        "description": inc.description,
        "short_description": inc.short_description
    }
    # POST-Request an ServiceNow-API
    response = requests.post(url, auth=(USERNAME_SN, PASSWORD_SN), headers=headers, json=incident_data)

    # Überprüfung und Ausgabe
    if response.status_code == 201:
        return incident_data
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Fehler beim Erstellen des Incidents: {response.text}")


# PUT-Methode für die Änderung bereits existierender Incidents
@incident.patch("/update_incident/{number}", status_code=status.HTTP_200_OK, response_model=schemas.Incident)
def update_incident(inc: schemas.UpdateIncident, number: str):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"
            }
    url = f"https://{INSTANCE}.lab.service-now.com/api/now/table/incident/{number}"

    # Abrufung des Incidents 
    existing_incident = _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="number", filter_element=number, with_sys_id= True)

    if not existing_incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incident {number} kann nicht gefunden werden!")
    else:
        sys_id = existing_incident[0].get("sys_id")
        print(f"Sys_ID: {sys_id}")

     # Nur die zu aktualisierenden Felder im Request-Body senden
    update_data = {
        "description": inc.description,
        "short_description": inc.short_description
    }

    # PUT-Request an ServiceNow-API
    url = f"https://{INSTANCE}.lab.service-now.com/api/now/table/incident/{sys_id}"
    response = requests.patch(url, auth=(USERNAME_SN, PASSWORD_SN), headers=headers, json=update_data)

    # Überprüfen und Ausgabe
    if response.status_code == 200:
        return update_data
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Fehler beim Aktualisieren des Incidents: {response.text}")
    


