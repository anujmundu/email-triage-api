from flask import Flask, request, jsonify
from ai_classifier import classify_email
from utils import validate_ai_output
from decision_logic import apply_rules
from storage import store_email
from actions import take_action

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
    <html>
      <head>
        <title>Email Triage API</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 80px;
            background-color: #f4f6f8;
            color: #333;
          }
          h1 { color: #2c3e50; }
          p { font-size: 18px; }
          a {
            display: inline-block;
            margin: 10px;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
          }
          a:hover { background-color: #2980b9; }
        </style>
      </head>
      <body>
        <h1>Email Triage API is running</h1>
        <p>Use the links below to test endpoints:</p>
        <a href="/health">Check API Health</a>
        <a href="/triage-email">Test Email Triage</a>
      </body>
    </html>
    """

@app.route("/health", methods=["GET"])
def health():
    return """
    <html>
      <head>
        <title>API Health</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            text-align: center;
            margin-top: 100px;
            color: #333;
          }
          .card {
            display: inline-block;
            padding: 30px;
            border-radius: 10px;
            background-color: #2ecc71;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
          }
          h1 { margin: 0; }
          p { font-size: 18px; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>API Health Check</h1>
          <p>Status: OK</p>
        </div>
      </body>
    </html>
    """

@app.route("/triage-email", methods=["GET", "POST"])
def triage_email():
    if request.method == "GET":
        return """
        <html>
          <head><title>Email Triage Test</title></head>
          <body style="font-family: Arial; margin: 40px;">
            <h2>Test Email Triage</h2>
            <form action="/triage-email" method="post">
              <label>Sender:</label><br>
              <input type="text" name="sender" required><br><br>
              <label>Subject:</label><br>
              <input type="text" name="subject" required><br><br>
              <label>Body:</label><br>
              <textarea name="body" required></textarea><br><br>
              <button type="submit">Submit</button>
            </form>
          </body>
        </html>
        """
    elif request.method == "POST":
        # Safely get JSON or form data
        data = request.get_json(silent=True) or {}
        email = {
            "sender": request.form.get("sender") or data.get("sender"),
            "subject": request.form.get("subject") or data.get("subject"),
            "body": request.form.get("body") or data.get("body")
        }

        # Validate input
        if not email["sender"] or not email["subject"] or not email["body"]:
            return jsonify({"error": "Missing required fields"}), 400

        ai_output = classify_email(email)

        if not validate_ai_output(ai_output):
            return jsonify({"error": "Invalid AI output"}), 400

        decision = apply_rules(ai_output)
        store_email(email, ai_output, decision)
        take_action(decision, email)

        return jsonify({"decision": decision})

    # Fallback: if neither GET nor POST matched
    return jsonify({"error": "Unsupported method"}), 405


from storage import get_all_emails, get_by_decision, count_by_intent

@app.route("/analytics/recent", methods=["GET"])
def recent_emails():
    emails = get_all_emails(limit=5)
    return jsonify(emails)

@app.route("/analytics/decisions/<decision>", methods=["GET"])
def decisions(decision):
    emails = get_by_decision(decision, limit=10)
    return jsonify(emails)

@app.route("/analytics/intents", methods=["GET"])
def intents_summary():
    summary = count_by_intent()
    return jsonify(summary)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
