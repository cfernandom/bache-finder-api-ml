from fastapi import FastAPI
from app.api.endpoints import predict

app = FastAPI()

app.include_router(predict.router, prefix="/predict")

@app.get("/")
async def root():
    return {"message": "Welcome to the Bache Finder API!"}