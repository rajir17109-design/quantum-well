# ⚛️ QuantumWell — AI Productivity & Wellness Assistant

> **Google Cloud Gen AI Academy APAC 2026 — Cohort 1 Hackathon**
> Built with ❤️ by **Team Quantum Coders** 🚀

[![Built with Gemini](https://img.shields.io/badge/Built%20with-Gemini%202.5%20Flash-4285F4?style=flat-square&logo=google)](https://deepmind.google/technologies/gemini/)
[![Powered by Vertex AI](https://img.shields.io/badge/Powered%20by-Vertex%20AI-34A853?style=flat-square&logo=google-cloud)](https://cloud.google.com/vertex-ai)
[![Deployed on Cloud Run](https://img.shields.io/badge/Deployed%20on-Cloud%20Run-FBBC04?style=flat-square&logo=google-cloud)](https://cloud.google.com/run)
[![Framework](https://img.shields.io/badge/Framework-Google%20ADK-EA4335?style=flat-square)](https://google.github.io/adk-docs/)

---

## 📖 Overview

**QuantumWell** is a multi-agent AI-powered productivity and wellness assistant that lets you track your diet, log workouts, manage tasks, and get intelligent daily progress reports — all through natural conversation.

No rigid forms. No complicated UIs. Just chat.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🥗 **Diet Tracking** | Log meals in plain language — calories estimated automatically |
| 💪 **Workout Logging** | Track runs, push-ups, yoga, and more with duration & calorie estimates |
| ✅ **Task Management** | Add, view, and manage your to-do list conversationally |
| 📊 **Progress Reports** | Get a smart daily summary with a wellness score and actionable tips |
| 📧 **Email Integration** | Connect Gmail to check and summarize important emails |
| 📅 **Schedule Management** | View upcoming meetings, events, and calendar entries conversationally |

---

## 🤖 Multi-Agent Architecture

QuantumWell uses a **multi-agent orchestration** pattern powered by **Google ADK** and **Gemini 2.5 Flash**. Each agent is specialized for a domain, and the Orchestrator routes every user message to the right agent automatically.

```
User Message
     │
     ▼
┌─────────────────────┐
│   Orchestrator      │  ← Routes intent to the right agent
└──────┬──────────────┘
       │
    ______________________________________________________                                           
  |▼           ▼           ▼           ▼         ▼          |▼
Diet       Workout      Task       Progress  Email    Schedule
Agent      Agent        Agent      Agent     Agent     Agent
```

| Agent | Responsibility |
|---|---|
| 🎯 **Orchestrator** | Classifies user intent and delegates to the right agent |
| 🥗 **Diet Agent** | Parses meal descriptions, estimates calories, tracks against daily goal |
| 💪 **Workout Agent** | Logs exercises, estimates duration and calories burned |
| ✅ **Task Agent** | Manages a dynamic task list with CRUD operations |
| 📊 **Progress Agent** | Aggregates daily data into a wellness score and personalized tips |
| 📧 **Email Agent** | Integrates with Gmail via OAuth to surface important messages |
| 📅 **Schedule Agent** | Retrieves calendar events, upcoming meetings, and daily schedule |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **AI Model** | Gemini 2.5 Flash (via Vertex AI) |
| **Agent Framework** | Google Agent Development Kit (ADK) |
| **Backend** | FastAPI (Python) |
| **Deployment** | Google Cloud Run |
| **Frontend** | HTML / CSS / JavaScript |
| **Email Integration** | Gmail API (OAuth 2.0) |
| **Calendar Integration** | Google Calendar API |

---

## 🧪 Agent Interaction Examples

Here are real interactions captured during testing:

**Diet Logging**
```
User:   I had 2 pizza and 1 coke in my dinner
Agent:  🍕 2 slices of pizza: ~560 kcal
        🥤 1 Coke: ~150 kcal
        Total: 710 kcal | Remaining: 1290 kcal of your 2000 kcal goal ✨
```

**Workout Logging**
```
User:   I did 4km and 30 pushups
Agent:  🏃 Running (4km) + 🏋️ Push-ups (30 reps)
        ⏱️ Duration: ~25–30 min | 🔥 Calories Burned: ~250 kcal
```

**Daily Progress Report**
```
User:   How was my day?
Agent:  📊 Daily Report for 2026-04-06
        🥗 Diet: 710 kcal logged
        💪 Workout: 4km run + 30 push-ups (~200 kcal burned)
        ✅ Tasks: 1 pending
        🌟 Today's Score: 6/10 — Great job getting your workout in!
```

**Task Management**
```
User:   Add task - complete assignment
Agent:  Got it! Added 'complete assignment' to your tasks. 👍

User:   Show all my tasks
Agent:  📚 complete assignment
```

**Schedule Check**
```
User:   What's on my calendar?
Agent:  📅 Here's your upcoming schedule:
        No meetings found for today — your calendar is clear! 🗓️✨
        Tip: Connect your Google Calendar to surface upcoming events here.

User:   What are my upcoming meetings?
Agent:  I checked your schedule — no upcoming meetings at the moment. 😄
        You can ask me anytime: "What's on my calendar tomorrow?"
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google Cloud project with Vertex AI & Cloud Run APIs enabled
- Gmail API credentials (for email integration)

### Installation

```bash
# Clone the repository
git clone https://github.com/rajir17109-design/quantum-well.git
cd quantum-well

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your Google Cloud project credentials
```

### Running Locally



Open your browser at `http://localhost:8080`

### Deploying to Cloud Run

```bash
# Build and push the container
gcloud builds submit --tag gcr.io/career-advisor-491804/quantum-well

# Deploy to Cloud Run
gcloud run deploy quantum-well \
  --image gcr.io/career-advisor-491804/quantum-well \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated
```

---

## 📁 Project Structure

```
quantum-well/
├── agents/
│   ├── orchestrator.py      # Intent routing
│   ├── diet_agent.py        # Meal tracking & calorie estimation
│   ├── workout_agent.py     # Exercise logging
│   ├── task_agent.py        # To-do management
│   ├── progress_agent.py    # Daily summary & scoring
│   ├── email_agent.py       # Gmail integration
│   └── schedule_agent.py    # Calendar & meeting queries
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── main.py                  # FastAPI app entrypoint
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 👥 Team Quantum Coders
 
Built for the **Google Cloud Gen AI Academy APAC 2026 — Cohort 1 Hackathon**.
 
We're a team passionate about making AI genuinely useful in everyday wellness and productivity.
 
| Name | Role | GitHub |
|---|---|---|
|🧑‍💻 **Amaresh Pal** | Team Member | [@amaresh-pal](https://github.com/amaresh-pal)  |
| 🧑‍💻 **Noah Tatpi** | Team Member | [@Noahtatpati](https://github.com/Noahtatpati) |
| 🧑‍💻 **Rajeshwari R** | Team Member | [@rajir17109-design](https://github.com/rajir17109-design) |
 



