from fastapi import FastAPI
from app.presentation.api import tasks

app = FastAPI()

app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
