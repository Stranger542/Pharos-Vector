from fastapi import FastAPI
from app.api.v1.fake_news import router as fake_news_router
from app.api.v1.media_literacy import router as media_literacy_router
from app.api.v1.source import router as source_router
from app.api.v1.claims import router as claims_router
from app.api.v1.user import router as user_router

app = FastAPI(
    title="Fake News Detection & Media Literacy Platform",
    version="1.0.0"
)

app.include_router(fake_news_router, prefix="/api/v1/fake-news")
app.include_router(media_literacy_router, prefix="/api/v1/learning")
app.include_router(source_router, prefix="/api/v1/source")
app.include_router(claims_router, prefix="/api/v1/claims")
app.include_router(user_router, prefix="/api/v1/user")
