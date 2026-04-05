from google import genai
from datetime import datetime

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

workouts = []

def workout_agent(user_input: str) -> str:
    prompt = f"""
You are a workout tracking AI assistant.

Current workouts today: {workouts}
User said: "{user_input}"
Current time: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Do the following:
1. Identify the exercise mentioned
2. Estimate calories burned
3. Log the workout
4. Give a short friendly response with:
   - Exercise logged
   - Duration
   - Calories burned
   - Total workouts today
   - One motivational tip

Keep response short and friendly. Use emojis.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    workouts.append(user_input)
    return response.text.strip()
