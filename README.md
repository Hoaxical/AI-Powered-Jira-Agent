AI-Powered-Jira-Agent
A web application that fetches Jira epics and generates AI-driven user stories and test cases. The frontend displays a human-readable AI response, while the raw JSON is saved on the backend.

Team members involved in this assignment:

Hemant Boodhun - Team Leader, Documentation Specialist, Backend & Frontend Developer (50% Overlap), Presentation Lead
Akhilesh Rewa - AI Engineer
Jayesh Aumeer - Backend Engineer, Frontend development assistance
Narvesh Chuttoor - Test Engineer


This is a readme file. (for installation guide/documentation purpose)

You will need to install these packages in case if you don't have them yet:
(Use a terminal if offered by your code editor, else best option to use Command Prompt)
- Flask
- dotenv
- google-generativeai
- requests
- flask_cors

You may run the following line in CMD for ease of installation:
pip install flask python-dotenv google-generativeai requests flask-cors

I apologise in case I missed a package you should install.



Installation Guide (continued):

In case if you don't see a '.env' file in the root directory (due to .gitignore), PLEASE FOLLOW THESE CRUCIAL STEPS:

1) Create a file '.env'
2) Create a variable 'ai_APIkey' and assign the following token to it: AIzaSyC0PyYOfJLpGyMNQEzmjNKiLiPybhfUpBg //(without any ' " ') OR Head over to Google AI Studio and create an API Key to use it.
3) Create another variable 'jira_APIkey' and assign an API key, given by your Jira account.
The following Jira API Key might get revoked/be expired if another person uses it, but as a precautionary measure, I have shared it: ATATT3xFfGF07_NKdq9VFA-AKuiqlSx1AhpvFj71R0EZ1C0_6gtUCPfBLxr66RZBp9fs6gtQbz7S-2dIWlYvqumkEeLw94-T70VvovrobeRGQ9SG5yqHBgGFxGfI1FvPxPEVwoEfwwezb0rQFDSXb0Qp2SWeiI_UoKl819vBdbiEz8xQ3O_5vTo=27A9A77C



NEXT:

Head over to /backend/fetch_api.py and put your own username (email address linked to your Jira account, also from which you generated an API Key) into 'username' variable.

Keep the same 'url' endpoint, DO NOT CHANGE IT.

(OPTIONAL): Head over to /ai/ai_agent.py and you may change the GenerativeModel. 

For now, "gemini-2.0-flash" is being used for faster response. You could use "gemini-2.0-pro" or "gemini-2.5-flash" or "gemini-2.5-pro", etc. But it could slow down response/prone to more errors.



Main steps to run the web app now:

1) Head over to backend/main_server.py

2) Run the flask server

3) Head over to frontend/index.html and open it using default browser (NOTE: DO NOT OPEN IT WITH LIVE SERVER, IT WILL CAUSE RELOAD ISSUES)

4) Now you may refresh/click on different epics and click generate.



Do note that, web interface will display the human readable format of the ai response. If you want to see the raw ai response, please head over to backend/ai_response.json which contains the JSON format AI Response (the real AI response).

Necessary comments have already been added in the code (documentation)