from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SourceInput(BaseModel):
    domain: str

@router.post("/credibility")
def get_source_credibility(source: SourceInput):
    # Placeholder: Integrate with NewsGuard API or similar
    # In production, replace with actual external API call
    mock_score = 85  # Example trust score
    return {
        "domain": source.domain,
        "trust_score": mock_score,
        "summary": "This source has a strong reputation for factual reporting."
    }
