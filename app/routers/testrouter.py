from fastapi import APIRouter, HTTPException
router = APIRouter(
    prefix="/test",
    tags=["Router"]
)


@router.get("/")
def hello_world_TEST():
    return {"Hello ITSM!!!"}