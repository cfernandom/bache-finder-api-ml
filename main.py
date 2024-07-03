from fastapi import FastAPI
from app.api.endpoints import predict
from app.api.endpoints.project1 import predicts as project1_predicts

app = FastAPI()

app.include_router(predict.router, prefix="/predict")
app.include_router(project1_predicts.router, prefix="/project1/predicts")

@app.get("/")
async def root():
    return {"message": "Welcome to the Bache Finder API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)