from fastapi import FastAPI
from .routers import incident
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
origins = [
        "http://localhost",
        "http://127.0.0.1",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "https://beleg.azurewebsites.net"
        "https://itsmgruppe1.azurewebsites.net"
    ]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get("/")
def root():
    return "Server is running"
 
app.include_router(incident.incident)