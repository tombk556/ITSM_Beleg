from fastapi import APIRouter, HTTPException
import requests
from ..config import settings

router = APIRouter(
    prefix="/servicenow",
    tags=["servicenow"]
)

INSTANCE = settings.instance_sn
USERNAME_SN = settings.username_sn
PASSWORD_SN = settings.password_sn


@router.get("/get_incident")
def get_incidents():
    return _incidents(INSTANCE, USERNAME_SN, PASSWORD_SN)


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
