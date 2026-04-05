from agents.progress_agent import progress_agent

diet_logs = [
    "2 idlis and sambar - 220 kcal",
    "Rice and dal - 540 kcal",
    "Banana - 90 kcal"
]

workout_logs = [
    "Running 3km - 180 kcal",
    "Yoga 30 mins - 120 kcal"
]

tasks = [
    {"task": "Complete ADK codelabs", "status": "done"},
    {"task": "Prepare PPT slides", "status": "pending"},
    {"task": "Push code to GitHub", "status": "done"}
]

print(progress_agent(diet_logs, workout_logs, tasks))
