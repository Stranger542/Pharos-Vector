from pydantic import BaseModel
from typing import Optional

class ClaimBase(BaseModel):
    article_id: int
    claim_text: str

class ClaimCreate(ClaimBase):
    pass

class ClaimRead(ClaimBase):
    id: int
    verdict: Optional[str] = None
    checked_by: Optional[str] = None
    checked_at: Optional[str] = None  # ISO format

    class Config:
        orm_mode = True

class ClaimUpdate(BaseModel):
    verdict: Optional[str] = None
    checked_by: Optional[str] = None
    checked_at: Optional[str] = None
