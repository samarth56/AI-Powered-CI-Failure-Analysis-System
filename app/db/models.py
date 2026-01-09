from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String(255), index=True)
    raw_log = Column(Text)

    ai_root_cause = Column(Text, nullable=True)  
    ai_solution = Column(Text, nullable=True)    

    created_at = Column(DateTime, default=datetime.utcnow)
