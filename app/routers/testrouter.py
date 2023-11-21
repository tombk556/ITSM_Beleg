from fastapi import APIRouter, HTTPException
router = APIRouter(
    prefix="/test",
    tags=["Router"]
)


@router.get("/{loc}")
def hello_world_TEST(loc: str):
    if loc == "GERMANY":
        return {"Hello World nach GERMANY"}
    else:
        return {"Hello World an alle!!!"}