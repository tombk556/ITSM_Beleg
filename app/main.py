from fastapi import FastAPI
from .routers import testrouter, servicenow


app = FastAPI()
app.include_router(testrouter.router)
app.include_router(servicenow.router)