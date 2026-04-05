from google import genai
from datetime import datetime

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

def diet_agent(user_input: str) -> str:
    prompt = f"""
You are a diet tracking AI assistant.

The user said: "{user_input}"

Do the following:
1. Identify the food items mentioned
2. Estimate calories for each item
3. Give a short friendly response with:
   - What was logged
   - Total calories
   - How many calories remaining (assume daily goal is 2000 kcal)
   - One short nutrition tip

Keep response short and friendly. Use emojis.
Today's date: {datetime.now().strftime("%Y-%m-%d")}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
