from fastapi import APIRouter, status, HTTPException
from ..config import settings
from .. import schemas
from datetime import datetime, timedelta
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

@incident.get("/get_incident_by_sys_id/{sys_id}")
def get_incident_by_number(sys_id: str):
    return _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="sys_id", filter_element=sys_id)


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

def _get_incident(instance, user, pwd, filter, filter_element):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    if filter == "number" or filter == "sys_id" or filter == "sys_id" or filter == "incident_state":
        url = f"https://{instance}.lab.service-now.com/api/now/table/incident?{filter}={filter_element}"
    else:
        url = f"https://{instance}.lab.service-now.com/api/now/table/incident"
        
    try:
        response = requests.get(url, auth=(user, pwd), headers=headers)

        if response.status_code != 200:
            return {
                "Status": response.status_code,
                "Error Response": response.json()
            }
        else:
            return incident_data(response.json())

    except Exception as error:
        return {
            "Status": "Intenal Server Error",
            "Error Response": error
        }

def incident_data(data):
    incidents = []

    for result_item in data["result"]:
        incident = {
            "sys_id": result_item.get("sys_id"),
            "number": result_item.get("number"),
            "date": result_item.get("sys_updated_on"),
            "short_description": result_item.get("short_description"),
            "description": result_item.get("description"),
            "state": result_item.get("incident_state")
        }
        
        incidents.append(incident)

    return incidents


@incident.get("/get_incidents_since/{time_data}")
def get_incident_by_date(time_data: str):
    data = get_incidents("date")

    if time_data == "yesterday":
        # Der aktuelle Tag
        current_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # Vortag
        yesterday = current_day - timedelta(days=1)

        filtered_data = [entry for entry in data if datetime.strptime(entry["date"], "%Y-%m-%d %H:%M:%S") >= yesterday]
        return filtered_data 
    
    elif "-" in time_data:
        try:
            mydate = datetime.strptime(time_data, "%Y-%m-%d")
            filtered_data = [entry for entry in data if datetime.strptime(entry["date"], "%Y-%m-%d %H:%M:%S").date() >= mydate.date()]
            return filtered_data 
        except ValueError:
            return {"error": "Ungültiges Datumsformat. Verwenden Sie das Format %Y-%m-%d."}
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Ungültiges Datumsformat. Verwenden Sie das Format %Y-%m-%d oder yesterday")

# POST-Methode zur Erstellung neuer Incidents

@incident.post("/create_incident", status_code=status.HTTP_201_CREATED, response_model=schemas.Incident)
def create_incident(inc: schemas.CrUpIncident):
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
        return _single_incident(response.json())
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Fehler beim Erstellen des Incidents: {response.text}")


def _single_incident(data):
    result_item = data["result"]
    incident = {
            "sys_id": result_item.get("sys_id"),
            "number": result_item.get("number"),
            "date": result_item.get("sys_updated_on"),
            "short_description": result_item.get("short_description"),
            "description": result_item.get("description"),
            "state": result_item.get("incident_state")
        }
    return incident

# PUT-Methode für die Änderung bereits existierender Incidents
@incident.patch("/update_incident/{sys_id}", status_code=status.HTTP_200_OK, response_model=schemas.Incident)
def update_incident(inc: schemas.CrUpIncident, sys_id: str):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"
            }
    
    # Abrufung des Incidents 
    existing_incident = _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="sys_id", filter_element=sys_id)

    if not existing_incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incident {sys_id} kann nicht gefunden werden!")

    update_data = {
        "description": inc.description,
        "short_description": inc.short_description
    }

    # PUT-Request an ServiceNow-API
    url = f"https://{INSTANCE}.lab.service-now.com/api/now/table/incident/{sys_id}"
    response = requests.patch(url, auth=(USERNAME_SN, PASSWORD_SN), headers=headers, json=update_data)

    # Überprüfen und Ausgabe
    if response.status_code == 200:
        return _single_incident(response.json())
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Fehler beim Aktualisieren des Incidents: {response.text}")
    

# DELETE-Methode für das Löschen bereits existierender Incidents
@incident.delete("/delete_incident/{sys_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(sys_id: str):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"
            }

    # Abrufung des Incidents 
    existing_incident = _get_incident(INSTANCE, USERNAME_SN, PASSWORD_SN, filter="sys_id", filter_element=sys_id)

    if not existing_incident:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incident mit der ID {sys_id} kann nicht gefunden werden!")

    # DELETE-Request an ServiceNow-API
    url = f"https://{INSTANCE}.lab.service-now.com/api/now/table/incident/{sys_id}"
    response = requests.delete(url, auth=(USERNAME_SN, PASSWORD_SN), headers=headers)

    # Überprüfen und Ausgabe
    if response.status_code == 204:
        return None
    else:
        raise HTTPException(status_code=response.status_code, detail=f"Fehler beim Löschen des Incidents: {response.text}")
