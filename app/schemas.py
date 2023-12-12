from pydantic import BaseModel

class Incident(BaseModel):
    short_description : str
    description : str

class CreateIncident(Incident):
    class Config:
        orm_mode = True