import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.orchestrator import orchestrator_agent
from agents.diet_agent import diet_agent
from agents.workout_agent import workout_agent
from agents.task_agent import task_agent
from agents.progress_agent import progress_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

diet_logs = []
workout_logs = []
tasks = []

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.message
    if not user_input:
        return {"response": "Please say something!"}

    agent = orchestrator_agent(user_input)
    print(f"Routing to: {agent}")

    if "DIET" in agent:
        response = diet_agent(user_input)
        diet_logs.append(user_input)
    elif "WORKOUT" in agent:
        response = workout_agent(user_input)
        workout_logs.append(user_input)
    elif "TASK" in agent:
        response = task_agent(user_input)
    elif "PROGRESS" in agent:
        response = progress_agent(diet_logs, workout_logs, tasks)
    else:
        response = "I'm not sure what you mean. Try saying something about diet, workout, tasks or progress! 😊"

    return {"response": response, "agent_used": agent}

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse("frontend/index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
