from fastapi import FastAPI
from .routers import servicenow, testrouter

app = FastAPI()

@app.get("/")
def root():
    return "Server is running"

# app.include_router(testrouter.router)
# app.include_router(servicenow.router)