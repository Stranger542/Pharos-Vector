from sqlmodel import SQLModel, Field
from typing import Optional

class Source(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    domain: str
    trust_score: Optional[int] = None
    reputation_summary: Optional[str] = None
