from fastapi import APIRouter


router = APIRouter(tags=["healthcheck"])


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "running"}
