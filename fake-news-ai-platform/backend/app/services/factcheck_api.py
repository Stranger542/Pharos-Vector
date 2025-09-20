import requests
from app.core.config import settings

FACTCHECK_API_URL = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

def search_fact_checks(query: str):
    params = {
        'query': query,
        'key': settings.FACTCHECK_API_KEY
    }
    response = requests.get(FACTCHECK_API_URL, params=params, timeout=5)
    if response.status_code == 200:
        data = response.json()
        return data.get("claims", [])
    else:
        return {"error": f"Fact check API error: {response.status_code}"}
