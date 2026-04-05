from agents.task_agent import task_agent

tests = [
    "Add task - complete ADK codelabs",
    "Add task - prepare PPT slides",
    "Show all my tasks",
    "Mark complete ADK codelabs task"
]

for t in tests:
    print(f"Input: {t}")
    print(f"Response: {task_agent(t)}")
    print("---")
