from pydantic import BaseModel


# Read Incident
class Incident(BaseModel):
    sys_id: str
    number: str
    short_description : str
    description : str


# Create and Update Incident
class CrUpIncident(BaseModel):
    short_description : str
    description : str
    class Config:
        orm_mode = True







