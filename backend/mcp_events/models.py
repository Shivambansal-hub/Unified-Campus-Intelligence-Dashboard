from pydantic import BaseModel
from typing import Optional, List


class Event(BaseModel):
    id: int
    title: str
    club: str
    date: str
    time: str
    venue: str
    description: str
    category: str  # tech, cultural, sports, academic, social
    registration_link: Optional[str] = None
    is_free: bool = True
    fee: float = 0
    max_participants: Optional[int] = None
    current_registrations: int = 0
    tags: List[str] = []


class Club(BaseModel):
    id: int
    name: str
    category: str
    description: str
    member_count: int
    contact_email: str
