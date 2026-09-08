#!/usr/bin/env python3
"""
CorrespondIQ - Intelligent Email & Calendar Briefing
"""
from googleapiclient.discovery import build
from gmail_auth import authenticate_google, fetch_important_emails
from calendar_auth import fetch_this_week_calendar
from ai_processor import get_ai_briefing  # <-- NOTE: Changed to 'processor'

def main():
    print(" CorrespondIQ is booting up...")
    print(" Authenticating with Google...")
    
    # Step 1: Authenticate
    creds = authenticate_google()
    
    # Step 2: Build API services
    gmail_service = build('gmail', 'v1', credentials=creds)
    calendar_service = build('calendar', 'v3', credentials=creds)
    
    print(" Fetching most important emails...")
    emails = fetch_important_emails(gmail_service)
    
    print("📅 Fetching this week's calendar...")
    meetings = fetch_this_week_calendar(calendar_service)
    
    if not emails:
        print(" No important unread emails found. Taking a break!")
        return
    
    print("🧠 Asking AI to synthesize your briefing...")
    briefing = get_ai_briefing(emails, meetings)
    
    # Print the final beautiful output
    print("\n" + "="*60)
    print(" YOUR CORRESPONDIQ DAILY BRIEFING")
    print("="*60)
    
    for item in briefing:
        print(f"\n🔹 {item['client']}")
        print(f"    {item['summary']}")
        print(f"    Action: {item['action']}")
        if item.get('meeting_scheduled'):
            print(f"   📆 Meeting: {item['meeting_scheduled']}")
        print("-" * 40)
    
    print("\n CorrespondIQ has completed its analysis. Have a productive day!")

if __name__ == "__main__":
    main()