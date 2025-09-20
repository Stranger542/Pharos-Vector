from pydantic import BaseModel
from typing import Optional

class ArticleBase(BaseModel):
    title: str
    text: str
    author: Optional[str] = None
    published_at: Optional[str] = None  # ISO format

class ArticleCreate(ArticleBase):
    pass

class ArticleRead(ArticleBase):
    id: int
    source_id: Optional[int]
    credibility_score: Optional[float] = None
    created_at: Optional[str] = None

    class Config:
        orm_mode = True

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
    credibility_score: Optional[float] = None
