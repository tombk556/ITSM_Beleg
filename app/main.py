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
    return {"Server is running - Version 0.14.1 - Please make sure your ServiceNow Lab Instance is running"}


app.include_router(incident.incident)
