from agents.orchestrator import orchestrator_agent

tests = [
    "I had dosa for breakfast",
    "I ran 3km today",
    "Add task - finish project",
    "Any important mails?",
    "How was my week?"
]

for t in tests:
    result = orchestrator_agent(t)
    print(f"Input: {t}")
    print(f"Routes to: {result}")
    print("---")
