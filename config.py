import os
from dotenv import load_dotenv

# Loading environment variables from the .env file in the root directory
load_dotenv()

def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found ")
    return api_key
