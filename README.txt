BASIC RULE-BASED CHATBOT

Project files:
- main.py: Flask backend and rule-based responses
- templates/index.html: web interface that calls the Flask /chat endpoint
- requirements.txt: packages needed to run and deploy the app

RUN LOCALLY (Windows)
1. Install Python 3 if it is not already installed.
2. Open Command Prompt in this folder.
3. Create a virtual environment (recommended):
   py -m venv .venv
4. Activate it:
   .venv\Scripts\activate
5. Install dependencies:
   pip install -r requirements.txt
6. Start the app:
   python main.py
7. Open http://127.0.0.1:5000 in your browser.

Try: hello, how are you, what is your name, help, thanks, bye.

DEPLOYMENT NOTE
For a hosted service that runs Flask, use the start command:
   gunicorn main:app
Do not deploy with Flask debug mode enabled. The chatbot is rule-based and does not use a generative AI model.
