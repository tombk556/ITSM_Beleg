from fastapi import FastAPI
from .routers import incident
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
    return "Server is running - Version 0.13"
 
app.include_router(incident.incident)

