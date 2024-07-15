from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TicketCreate(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None


class TicketResponse(TicketCreate):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True