import requests
from app.core.config import settings

NEWSGUARD_API_URL = "https://api.newsguardtech.com/domain/"

def get_newsguard_report(domain: str):
    headers = {
        "Authorization": f"Bearer {settings.NEWSGUARD_API_KEY}"
    }
    url = f"{NEWSGUARD_API_URL}{domain}"
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to retrieve NewsGuard data: {response.status_code}"}
