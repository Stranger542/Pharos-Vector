from pydantic import BaseModel
from typing import Optional

class SourceBase(BaseModel):
    name: str
    domain: str

class SourceCreate(SourceBase):
    trust_score: Optional[int] = None
    reputation_summary: Optional[str] = None

class SourceRead(SourceBase):
    id: int
    trust_score: Optional[int] = None
    reputation_summary: Optional[str] = None

    class Config:
        orm_mode = True

class SourceUpdate(BaseModel):
    trust_score: Optional[int] = None
    reputation_summary: Optional[str] = None
