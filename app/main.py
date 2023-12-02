from fastapi import FastAPI, status
import requests
from .config import config
from . import schemas

INSTANCE = config.get("INSTANCE_SN")
USERNAME_SN = config.get("USERNAME_SN")
PASSWORD_SN = config.get("PASSWORD_SN")

app = FastAPI()

@app.get("/")
def root():
    return "Server is running"

@app.get("/get_incident")
def get_incidents():
    return _incidents(INSTANCE, USERNAME_SN, PASSWORD_SN)


@app.post("/create_incident", status_code=status.HTTP_201_CREATED, response_model=schemas.Incident)
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
            return response.json()

    except Exception as error:
        return {
            "Status": "Intenal Server Error",
            "Error Response": error
        }