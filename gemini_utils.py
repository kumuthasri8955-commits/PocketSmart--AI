import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

import time

def ask_gemini(prompt):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if attempt < 2:
                time.sleep(3)
            else:
                raise e
    return response.text