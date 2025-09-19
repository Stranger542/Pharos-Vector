from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LiteracyRequest(BaseModel):
    topic: str

@router.post("/deconstruct")
def deconstruct_news(request: LiteracyRequest):
    # Example placeholder: Return questions for user to consider
    topic = request.topic
    return {
        "questions": [
            f"Who created this message about {topic}?",
            "What techniques are used to attract your attention?",
            "Is this fact, opinion, or something else?",
            "Can you find alternate sources?"
        ]
    }
