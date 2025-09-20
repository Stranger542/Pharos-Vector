from sqlmodel import SQLModel, Field
from typing import Optional

class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    text: str
    author: Optional[str] = None
    published_at: Optional[str] = None  # ISO format string
    source_id: Optional[int] = Field(default=None, foreign_key="source.id")
    credibility_score: Optional[float] = None
    created_at: Optional[str] = None
