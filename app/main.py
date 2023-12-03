from fastapi import FastAPI
from .routers import incident
app = FastAPI()

app.include_router(incident.incident)

@app.get("/")
def root():
    return "Server is running"