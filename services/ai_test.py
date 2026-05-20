import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors

#To load the .env file
env_path = Path(__file__).resolve().parent.parent / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello, act like a financial assistant",
    )
    print("\n--- AI Response ---")
    print(response.text)
    print("-------------------\n")

except errors.ServerError as e:
    print(f"\n[Server Error]: Google servers are currently overloaded (503). Try again in a few minutes.")
except Exception as e:
    print(f"\n[Error]: {e}")