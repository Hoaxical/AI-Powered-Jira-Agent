import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# fetch api key safely
API_KEY = os.getenv("ai_APIkey")
genai.configure(api_key=API_KEY)

def call_gemini_and_parse(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # Generate AI response
    response = model.generate_content(prompt)
    text = response.text

    # Extract JSON part from the response
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
        "story_points": 3 (for example)
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
    return prompt
