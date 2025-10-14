import sys
import os
import json
from fetch_api import fetch_jiraAPI

# Add parent directory (project_root) to Python path BEFORE importing from ai
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.ai_agent import generate_stories_and_tests, call_gemini_and_parse


def main():
    # Fetch epics from Jira
    epics = fetch_jiraAPI()

    # Print only the first epic nicely formatted
    print(json.dumps(epics[1], indent=2))

    # Send to AI
    print("\nPrompting AI... Generating...\n")
    prompt = generate_stories_and_tests(epics[1]["name"], epics[1]["description"])
    jsonresponse = call_gemini_and_parse(prompt)

    print(json.dumps(jsonresponse, indent=2))



main()



'''for i in range(len(epics)):
        prompt = generate_stories_and_tests(epics[i]["name"], epics[i]["description"])
        call_gemini_and_parse(prompt)'''
