from agents.diet_agent import diet_agent

tests = [
    "I had 2 idlis and sambar for breakfast",
    "I ate rice and dal for lunch",
    "I had a banana as snack"
]

for t in tests:
    print(f"Input: {t}")
    print(f"Response: {diet_agent(t)}")
    print("---")
