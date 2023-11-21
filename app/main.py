from fastapi import FastAPI
from .routers import testrouter

app = FastAPI()

app.include_router(testrouter.router)