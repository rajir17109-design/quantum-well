from agents.workout_agent import workout_agent

tests = [
    "I ran 3km today",
    "Did 30 minutes of yoga",
    "20 pushups and 20 squats done"
]

for t in tests:
    print(f"Input: {t}")
    print(f"Response: {workout_agent(t)}")
    print("---")
