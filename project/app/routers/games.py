from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_description="test")
async def get_hello():
    return {"message": "hello"}
