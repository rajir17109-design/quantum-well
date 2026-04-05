from google import genai
from datetime import datetime

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

def progress_agent(diet_logs: list, workout_logs: list, tasks: list) -> str:
    prompt = f"""
You are a progress tracking AI assistant called QuantumWell.

Here is the user's data for today:
- Diet logs: {diet_logs}
- Workout logs: {workout_logs}
- Tasks: {tasks}
- Date: {datetime.now().strftime("%Y-%m-%d")}

Give a friendly daily progress report with:
1. 🥗 Diet Summary — total calories, how close to 2000 kcal goal
2. 💪 Workout Summary — exercises done, total calories burned
3. ✅ Task Summary — completed vs pending tasks
4. 🌟 Overall Score — rate the day out of 10
5. 💡 3 tips to improve tomorrow

Keep it motivating, friendly and short. Use emojis!
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
