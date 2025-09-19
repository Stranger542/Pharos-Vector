from sqlmodel import SQLModel, Field
from typing import Optional

class Claim(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    article_id: int = Field(foreign_key="article.id")
    claim_text: str
    verdict: Optional[str] = None
    checked_by: Optional[str] = None
    checked_at: Optional[str] = None  # ISO format string
