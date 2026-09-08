import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


#Handles Google login, stores sesssions, fetches important emails

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.readonly'
]

def authenticate_google():
    """Authenticate using OAuth 2.0 and store the token locally."""
    creds = None
    
    # token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # IMPORTANT: You must download your own credentials.json from Google Cloud Console
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def fetch_important_emails(service, max_results=10):
    """
    Fetch unread or important emails from Gmail.
    Returns a clean list of dicts with subject, sender, and preview.
    """
    result = service.users().messages().list(
        userId='me',
        q='is:unread OR is:important',  # Gmail's smart search
        maxResults=max_results
    ).execute()
    
    messages = result.get('messages', [])
    email_data = []
    
    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me', 
            id=msg['id'], 
            format='metadata'
        ).execute()
        
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        snippet = msg_data.get('snippet', 'No preview available.')
        
        email_data.append({
            "sender": sender,
            "subject": subject,
            "snippet": snippet
        })
    
    return email_data