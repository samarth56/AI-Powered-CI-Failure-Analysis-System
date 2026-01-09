from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Log
from app.services.ai_analyzer import analyze_log  # 👈 ADD THIS

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.post("/")
def create_log(
    raw_log: str = Body(..., media_type="text/plain"),
    db: Session = Depends(get_db)
):
    # 🔥 AI ANALYSIS STEP
    ai_result = analyze_log(raw_log)

    new_log = Log(
        test_name="Jenkins Failure",
        raw_log=raw_log,
        ai_root_cause=ai_result["root_cause"],
        ai_solution=ai_result["solution"]
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {
        "message": "Log analyzed and saved successfully",
        "root_cause": new_log.ai_root_cause,
        "solution": new_log.ai_solution
    }
