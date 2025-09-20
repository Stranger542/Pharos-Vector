from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ClaimInput(BaseModel):
    claim: str

@router.post("/verify")
def verify_claim(claim: ClaimInput):
    # Placeholder: Integrate with Google Fact Check Tools or News API
    # In production, replace with actual API/service call
    matches = [
        {"headline": "President did not say X", "source": "FactCheck.org", "verdict": "False"},
        {"headline": "Official data disproves claim", "source": "PolitiFact", "verdict": "Pants on Fire"}
    ]
    return {
        "claim": claim.claim,
        "checks": matches
    }
