import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

# Jira API endpoint
url = "https://hoaxical.atlassian.net/rest/api/3/search/jql?jql=project=DIN AND issuetype=Epic&fields=summary,description"

# Username and API key
username = "hoaxical@gmail.com"
#api_key = os.getenv("jira_APIkey")
api_key = "ATATT3xFfGF0hRxxZVp4sPVMHa8IG3nqorA4h_PvxtKxgUUy_LnzVQ2nGs3Y7dVR72nNjGSYfgbh98tTDupnuxNnntahznGUGeuhq7332_fzMRg7U2u7a4QCGGvKSEuggUnUu-gmcyChD81X8OykK6VKD5bb7aSE6p5SLQ2u5kRjUPKejZ6-CH4=BB6FBAA6"

def fetch_jiraAPI():

    print("🔍 Loaded from .env:")
    print("URL:", url)
    print("Username:", username)
    print("API key starts with:", api_key[:5])  # Don't print full key


    # Make a GET request to Jira API
    response = requests.get(url, auth=(username, api_key))
    print("Status code:", response.status_code)

    try:
        data = response.json()
    except Exception as exp:
        print("Failed to parse JSON:", exp)
        print("Response text:", response.text)
        return {}
    

    # Create a dictionary to store epics with their keys
    sorted_epics = {}

    for i in range(1, len(data["issues"]) + 1):

        for issue in data["issues"]:

            if issue["key"] == f"DIN-{i}":

                id = int(issue["id"])
                key = issue["key"]
                summary = issue["fields"]["summary"]
                description = issue["fields"]["description"]["content"][0]["content"][0]["text"]

                sorted_epics[i] = {
                    "id": id,
                    "key": key,
                    "name": summary,
                    "description": description
                }

                break

    return sorted_epics  # returns a dictionary for easy indexing

