from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("")
def pong():
    return {"message": "pong"}
