from fastapi import FastAPI
from .routers import incident
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()

# Set up CORS
origins = [
    "http://vuejs_frontend:8080",  # Use the service name defined in Docker Compose
    "https://beleg.azurewebsites.net",
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