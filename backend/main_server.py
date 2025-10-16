# backend/main_server.py

import sys
import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from fetch_api import fetch_jiraAPI

# Add parent directory for ai imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.ai_agent import generate_stories_and_tests, call_gemini_and_parse
from convertairesponse import convert_ai_response_to_text
 
app = Flask(__name__) #initialize Flask app
CORS(app)  #allow JS frontend to fetch
 
#this is the endpoint for the function to fetch all epics LIVE.. YES, LIVE from Jira API
@app.route("/refresh-epics", methods=["GET"])
def refresh_epics():
    epics = fetch_jiraAPI() #this fetches the epics from Jira API using the function in fetch_api.py and stores it in epics variable
    if not epics:
        return jsonify({"error": "No epics found"}), 404
    #skips the above codeblock if epics is not empty
    return jsonify(epics)

#this is the endpoint for the function to generate AI stories for an epic (epic_index is passed from the frontend)
@app.route("/generate-ai/<int:epic_index>", methods=["GET"])
def generate_ai(epic_index):
    epics = fetch_jiraAPI() #this fetches the epics from Jira API using the function in fetch_api.py and stores it in epics variable

    if epic_index not in epics:
        return jsonify({"error": f"Epic {epic_index} not found"}), 404
    
    #skip above codeblock if epic_index is valid
    epic = epics[epic_index]

    #step 1: generates prompt and gets AI response
    prompt = generate_stories_and_tests(epic["name"], epic["description"])
    #passes prompt to the function in ai_agent.py which returns the prompt string
    ai_response = call_gemini_and_parse(prompt) #stores the ai response inside ai_response variable

    #step 2: saves AI response to JSON file -- overwrites the json file every time
    output_path = os.path.join(os.path.dirname(__file__), "ai_response.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ai_response, f, indent=2, ensure_ascii=False)

    #step 3: converts the JSON response into human-readable text
    #calls the function from convertairesponse.py
    readable_text = convert_ai_response_to_text(ai_response)

    #step 4: it returns the readable text as a javascript object for the frontend (using javascript) to display
    return jsonify({
        "readable_text": readable_text
    })
  
#runs the Flask server
if __name__ == "__main__":
    app.run(debug=True)
