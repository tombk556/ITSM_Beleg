from fastapi import FastAPI, HTTPException, status
from .routers import incident
from .routers.incident import get_incidents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    incidents = get_incidents(type="date")
    if incidents:
        return HTTPException(status_code=status.HTTP_200_OK, 
                             detail="ServiceNow Credentials are valid and the ServiceNow Lab is running",
                             headers="Server is running - Version 0.14.1")
    else:
        return HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, 
                             detail="ServiceNow Credentials are not valid or the ServiceNow Lab is not running",
                             headers="Server is not running")


app.include_router(incident.incident)
