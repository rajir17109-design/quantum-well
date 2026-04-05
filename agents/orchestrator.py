from google import genai
import os

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

def orchestrator_agent(user_input: str) -> str:
    prompt = f"""
You are an AI productivity assistant called QuantumWell.
Analyze the user message and decide which agent to call:

- If about food, meals, calories, diet → reply with: DIET_AGENT
- If about exercise, workout, running, gym → reply with: WORKOUT_AGENT
- If about tasks, todo, remind, complete → reply with: TASK_AGENT
- If about emails, gmail, inbox, mail → reply with: EMAIL_AGENT
- If about progress, summary, report, week → reply with: PROGRESS_AGENT

User message: {user_input}

Reply with ONLY the agent name, nothing else.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()
