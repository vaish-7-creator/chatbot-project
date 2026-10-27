from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)


def chatbot_response(message):
    """Return a rule-based response for the user's message."""
    message = message.strip().lower()

    if not message:
        return "Please type a message so I can respond."

    # Match whole words so 'hi' does not accidentally match 'this'.
    words = set(re.findall(r"\b[a-z']+\b", message))

    if words.intersection({"hello", "hi", "hey"}):
        return "Hello! How can I help you?"
    elif "how are you" in message:
        return "I'm doing well, thank you! How can I help you today?"
    elif "your name" in message or "who are you" in message or "name" in words:
        return "I'm a simple rule-based chatbot built with Python and Flask."
    elif words.intersection({"bye", "goodbye"}):
        return "Goodbye! Have a great day!"
    elif "help" in words:
        return "You can greet me, ask how I am, ask my name, or say goodbye."
    elif "thank" in words or "thanks" in words:
        return "You're welcome!"
    elif "time" in words:
        return "I can't check the current time yet, but you can ask me about my basic features."
    else:
        return "Sorry, I don't understand that yet. Try saying hello, asking my name, or typing help."


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("message"), str):
        return jsonify({"error": "Please send a message as JSON."}), 400

    user_message = data["message"].strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty."}), 400

    return jsonify({"message": user_message, "reply": chatbot_response(user_message)})


if __name__ == "__main__":
    # Debug mode is for local development only; hosted deployment uses Gunicorn.
    app.run(host="127.0.0.1", port=5000, debug=True)
