from fastapi import FastAPI
from app.api.logs import router as log_router
from app.db.database import engine
from app.db import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Powered CI Failure Analysis System")

app.include_router(log_router)

@app.get("/health")
def health():
    return {"status": "UP"}
