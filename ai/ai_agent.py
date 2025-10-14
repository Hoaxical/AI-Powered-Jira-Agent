# ai_agent.py
import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file for API key
load_dotenv()

API_KEY = os.getenv("GENAI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

def call_gemini_and_parse(prompt):
    """
    Sends prompt to Gemini and ensures the result is valid JSON.
    """
    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(prompt)
    text = response.text

    # Try to extract JSON from response
    match = re.search(r"```json\s*(\{.*\})\s*```", text, re.S)
    if match:
        json_str = match.group(1)
    else:
        match = re.search(r"(\{.*\})", text, re.S)
        json_str = match.group(1) if match else None

    if not json_str:
        raise ValueError("Gemini did not return valid JSON:\n" + text[:500])

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("Failed to parse Gemini JSON:\n" + json_str[:500])


def generate_stories_and_tests(epic_title, epic_description, n_stories=4):
    """
    Convert an Epic into structured user stories and test cases.
    """
    prompt = f"""
You are an expert Agile Product Owner and QA Engineer.
Convert the following EPIC into {n_stories} user stories and for each story generate 2-3 test cases.

Return output as **strict JSON** in the format:
{{
  "epic_title": "",
  "epic_description": "",
  "user_stories": [
    {{
      "id": "US-1",
      "title": "",
      "description": "",
      "acceptance_criteria": [
        "Given ... When ... Then ..."
      ],
      "story_points": 3
    }}
  ],
  "test_cases": [
    {{
      "testcase_id": "TC-US-1-01",
      "story_id": "US-1",
      "preconditions": "",
      "steps": ["", ""],
      "expected_results": ""
    }}
  ]
}}

EPIC TITLE:
{epic_title}

EPIC DESCRIPTION:
{epic_description}
"""

    return call_gemini_and_parse(prompt)


# Example test run (only runs when this file executed directly)
if __name__ == "__main__":
    epic_title = "Guest Checkout Flow"
    epic_description = "Allow users to purchase without an account using card payments."
    output = generate_stories_and_tests(epic_title, epic_description)
    print(json.dumps(output, indent=2))

