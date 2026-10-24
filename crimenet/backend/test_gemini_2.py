import os
import json
import traceback
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.gemini_api_key)

try:
    model = genai.GenerativeModel('gemini-flash-latest')
    prompt = """
                Extract named entities from the following FIR text. 
                Identify ONLY people (PERSON), organizations (ORG), and locations/cities (LOCATION).
                Do not include generic words, verbs, or dates.
                For PERSON entities, also extract their Date of Birth (dob), nationality, and where they were last seen (last_seen) if available in the text.
                Return ONLY a raw JSON array of objects (no markdown, no backticks).
                Format: [{"type": "PERSON", "name": "John Doe", "dob": "1990-01-01", "nationality": "Indian", "last_seen": "Delhi"}, {"type": "LOCATION", "name": "Mumbai"}]
                
                Text:
                FIR No: 1026/2026
                Date: 31 August 2026

                --------------------------------------------------
                SUBJECT: INVESTIGATION REPORT - ILLEGAL ARMS RING

                INCIDENT DETAILS:
                Intelligence suggests a coordinated illegal arms smuggling operation functioning in Delhi. The operation is led by Vikram Singh, who has been observed at the abandoned warehouse in Okhla. 

                Vikram Singh regularly communicates with Amit Sharma, who acts as the primary distributor. Amit Sharma was recently seen meeting with members of the Shadow Cartel. 

                Call records also show Amit Sharma is in frequent contact with a supplier named Rohit Patel (Phone: +91-9876543210).

                PROFILE DETAILS:
                - Name: Vikram Singh
                - DOB: 12/04/1985
                - Nationality: Indian
                - Last Seen: 29 August 2026

                - Name: Amit Sharma
                - DOB: 02/09/1988
                - Nationality: Indian
                - Last Seen: 30 August 2026
    """
    
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
        )
    )
    
    print("RESPONSE:", response.text)
except Exception as e:
    print(traceback.format_exc())
