from fastapi import APIRouter, status, HTTPException
from ..config import settings
from .. import schemas
import requests

incident = APIRouter(
    prefix="/incident",
    tags=['Incident'])

INSTANCE = settings.instance_sn
USERNAME_SN = settings.username_sn
PASSWORD_SN = settings.password_sn


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


@incident.post("/create_incident", status_code=status.HTTP_201_CREATED, response_model=schemas.Incident)
def create_incident(inc: schemas.CreateIncident):
    return {
        "short_description": inc.short_description,
        "description": inc.description
    }


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
            return incident_data(data =response.json())

    except Exception as error:
        return {
            "Status": "Intenal Server Error",
            "Error Response": error
        }

def incident_data(data):
    incidents = []

    for result_item in data["result"]:
        incident = {
            "number": result_item.get("number"),
            "date": result_item.get("sys_updated_on"),
            "short_description": result_item.get("short_description"),
            "description": result_item.get("description"),
            "state": result_item.get("incident_state")
        }

        incidents.append(incident)

    return incidents