from fastapi import FastAPI
from api.view import router as pong_router

app = FastAPI()
app.include_router(pong_router)

