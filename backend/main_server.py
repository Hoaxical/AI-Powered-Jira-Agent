import sys
import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from fetch_api import fetch_jiraAPI

# Add parent directory for ai imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai.ai_agent import generate_stories_and_tests, call_gemini_and_parse

app = Flask(__name__)
CORS(app)  # Allow JS frontend to fetch

# Endpoint to fetch epics
@app.route("/refresh-epics", methods=["GET"])
def refresh_epics():
    epics = fetch_jiraAPI()
    if not epics:
        return jsonify({"error": "No epics found"}), 404
    return jsonify(epics)

# Optional: Endpoint to generate AI stories for a specific epic
@app.route("/generate-ai/<int:epic_index>", methods=["GET"])
def generate_ai(epic_index):
    epics = fetch_jiraAPI()
    if epic_index not in epics:
        return jsonify({"error": f"Epic {epic_index} not found"}), 404
    epic = epics[epic_index]

    prompt = generate_stories_and_tests(epic["name"], epic["description"])
    ai_response = call_gemini_and_parse(prompt)
    return jsonify(ai_response)


if __name__ == "__main__":
    app.run(debug=True)
