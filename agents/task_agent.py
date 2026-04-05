from google import genai
import json
from datetime import datetime

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

tasks = []

def task_agent(user_input: str) -> str:
    prompt = f"""
You are a task management AI assistant.

Current tasks: {json.dumps(tasks)}
User said: "{user_input}"
Current time: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Do the following:
1. Understand if user wants to:
   - ADD a task → extract task name and add it
   - COMPLETE a task → mark it done
   - VIEW tasks → list all pending tasks
   - DELETE a task → remove it

2. Update the task list accordingly
3. Give a short friendly response with:
   - What action was taken
   - Current pending tasks list

Keep response short. Use emojis.
Return response in this JSON format:
{{
  "response": "your friendly message here",
  "tasks": [updated tasks list]
}}
"""
    result = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    try:
        cleaned = result.text.strip().replace("```json","").replace("```","")
        data = json.loads(cleaned)
        tasks.clear()
        tasks.extend(data.get("tasks", []))
        return data.get("response", result.text)
    except:
        return result.text.strip()
