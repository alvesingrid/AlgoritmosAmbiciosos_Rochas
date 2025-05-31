from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    title: str
    start: datetime
    end: datetime
