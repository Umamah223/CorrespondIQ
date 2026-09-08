from datetime import datetime, timedelta

# Fetches calendar events for the next 7 days

def fetch_this_week_calendar(service):
    """Fetch all calendar events from today until the next 7 days."""
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    next_week = (datetime.utcnow() + timedelta(days=7)).isoformat() + 'Z'
    
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        timeMax=next_week,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])
    meeting_data = []
    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        attendees = event.get('attendees', [])
        attendee_emails = [att.get('email') for att in attendees][:3]  # First 3 attendees
        
        meeting_data.append({
            "summary": event.get('summary', 'Untitled Meeting'),
            "start": start,
            "attendees": attendee_emails
        })
    
    return meeting_data