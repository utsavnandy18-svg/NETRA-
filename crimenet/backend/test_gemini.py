import os
import json
import traceback
import google.generativeai as genai
from app.config import settings

print(f"Key from settings: {bool(settings.gemini_api_key)}")
print(f"Key from os.getenv: {bool(os.getenv('GEMINI_API_KEY'))}")

genai.configure(api_key=settings.gemini_api_key)

if os.getenv("GEMINI_API_KEY"):
    print("os.getenv('GEMINI_API_KEY') is Truthy!")
else:
    print("os.getenv('GEMINI_API_KEY') is Falsey! This skips Gemini.")

try:
    model = genai.GenerativeModel('gemini-flash-latest')
    res = model.generate_content('Extract named entities from the following FIR text. Format: [{"type": "PERSON", "name": "John Doe"}]. Text: Amit Sharma was caught today.')
    print(res.text)
except Exception as e:
    print(traceback.format_exc())
