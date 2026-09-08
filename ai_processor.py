import json
from google import genai
from google.genai import types
from config import get_gemini_api_key

def get_ai_briefing(emails, meetings):
    """Send emails and calendar to Gemini, get back a structured to-do list."""
    # Initialize the new client
    client = genai.Client(api_key=get_gemini_api_key())

    prompt = f"""
    You are "CorrespondIQ", an elite executive assistant AI.
    
    Here are my recent important emails (in JSON):
    {json.dumps(emails)}
    
    Here are my upcoming meetings for this week (in JSON):
    {json.dumps(meetings)}
    
    Analyze this data carefully. For each distinct client or sender mentioned in the emails, 
    provide a structured briefing.
    
    Your output MUST be a valid JSON list. Each item in the list must have:
    - "client": The name of the client/sender.
    - "summary": A very short (1 sentence) summary of the email thread.
    - "action": The single most important action I need to take right now.
    - "meeting_scheduled": Either "Yes, on [Day] at [Time]" or "No".
    
    Format strictly as JSON. Example:
    [
      {{
        "client": "Acme Corp",
        "summary": "They requested a revised proposal",
        "action": "Send the updated PDF by 5 PM today",
        "meeting_scheduled": "Yes, Thursday at 2 PM"
      }}
    ]
    """
    
    # Use a commonly available model
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    
    # Clean the response (Gemini sometimes wraps it in markdown code blocks)
    clean_json = response.text.replace('```json', '').replace('```', '').strip()
    
    try:
        return json.loads(clean_json)
    except json.JSONDecodeError:
        # Fallback in case Gemini gives plain text
        return [{"client": "Error", "summary": "AI returned invalid JSON", "action": "Check logs", "meeting_scheduled": "N/A"}]