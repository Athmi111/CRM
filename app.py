from flask import Flask, request, render_template, redirect, url_for
from wa_client import WAClient  # your WhatsApp client class

app = Flask(__name__)
wa = WAClient()

# Webhook route for WhatsApp Cloud API
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return request.args.get("hub.challenge", "")
    data = request.json
    print("Incoming message:", data)
    return {"status": "received"}

# Route to render index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route to handle sending a message
@app.route("/send-message", methods=["POST"])
def send_message():
    to = request.form["to"]
    text = request.form["text"]
    response = wa.send_text(to, text)
    print("Message sent:", response)
    return redirect(url_for("index"))

# Route to handle message generation
@app.route("/generate-message", methods=["POST"])
def generate_message():
    prompt = request.form["prompt"].lower()

    # Simple rules-based generator
    if "diwali" in prompt:
        msg = "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!"
    elif "birthday" in prompt:
        msg = "Hello {name}, Happy Birthday! Wishing you a fantastic year ahead."
    else:
        msg = "Hello {name}, " + prompt.capitalize()

    return render_template("index.html", generated_message=msg)

# ✅ Add this block so Flask actually runs
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
