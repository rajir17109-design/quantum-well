from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google import genai
import os
import json
import base64
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

client = genai.Client(
    vertexai=True,
    project="career-advisor-491804",
    location="us-central1"
)

def get_gmail_service():
    creds = None
    if os.path.exists('token_gmail.pickle'):
        with open('token_gmail.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_gmail.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def email_agent(user_input: str) -> str:
    try:
        service = get_gmail_service()
        results = service.users().messages().list(
            userId='me', maxResults=5, labelIds=['INBOX']).execute()
        messages = results.get('messages', [])

        emails = []
        for msg in messages:
            txt = service.users().messages().get(
                userId='me', id=msg['id']).execute()
            payload = txt['payload']
            headers = payload['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            emails.append(f"From: {sender} | Subject: {subject}")

        email_list = "\n".join(emails)

        prompt = f"""
You are an email assistant for QuantumWell.

Here are the user's recent emails:
{email_list}

User said: "{user_input}"

Do the following:
1. Categorize each email as Important 🔴 or Normal 🟡
2. Give a short summary of each
3. Highlight any that need urgent attention

Keep response short and friendly. Use emojis.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        return f"Email agent error: {str(e)}"
