from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserInput(BaseModel):
    username: str

@router.post("/profile")
def get_user_profile(user: UserInput):
    # Mock profile info. Integrate with authentication/session in production.
    return {
        "username": user.username,
        "saved_articles": [],
        "quiz_stats": {"total_quizzes": 0, "correct_answers": 0}
    }
