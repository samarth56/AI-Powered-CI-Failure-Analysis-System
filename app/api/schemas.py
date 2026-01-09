from pydantic import BaseModel

class LogCreate(BaseModel):
    test_name: str
    raw_log: str
