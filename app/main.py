from fastapi import FastAPI
from .routers import incident
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
# Configure CORS to allow requests from http://localhost:8081
origins = [
    "http://localhost:8081",
    # Add more allowed origins if needed
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