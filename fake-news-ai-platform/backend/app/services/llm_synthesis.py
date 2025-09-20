from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def synthesize_report(data: dict) -> str:
    # Compose prompt carefully based on data from detection, source, claims modules
    prompt = f"Given the following data, generate a clear and concise credibility report:\n{data}"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a neutral media literacy expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
