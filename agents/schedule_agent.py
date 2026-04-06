from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google import genai
import os
import pickle
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

def get_calendar_service():
    creds = None
    if os.path.exists('token_calendar.pickle'):
        with open('token_calendar.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_calendar.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def schedule_agent(user_input: str) -> str:
    try:
        service = get_calendar_service()
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=5,
            singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        event_list = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list.append(f"{start} - {event.get('summary', 'No title')}")

        prompt = f"""
You are a scheduling assistant for QuantumWell.

Upcoming events:
{chr(10).join(event_list) if event_list else 'No upcoming events'}

User said: "{user_input}"

Do the following:
1. If user wants to VIEW schedule → list upcoming events nicely
2. If user wants to ADD event → confirm what would be added
3. Give a short friendly response

Keep response short. Use emojis.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        return f"Schedule agent error: {str(e)}"
