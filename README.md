[README.md](https://github.com/user-attachments/files/22626847/README.md)
# WhatsApp CRM (Python + Flask)

A simple WhatsApp CRM built with **Flask** that lets you:
- Send WhatsApp messages via Cloud API
- Generate predefined messages (e.g., Diwali greetings, birthdays) from prompts
- Use a web-based frontend form for sending messages

---

## 📌 Requirements

- Python 3.9+  
- Flask  
- Requests  
- Waitress (optional, for production server)  
- Ngrok (if you want to expose locally to the internet)

Install dependencies:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should look like:

```
flask
requests
waitress
```

---

## 📌 Project Structure

```
whatsapp-crm/
│── app.py              # Main Flask application
│── wa_client.py        # WhatsApp API client
│── templates/
│    └── index.html     # Frontend form
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

---

## 📌 Environment Variables

Before running, set your environment variables (replace with your real values):

**Windows PowerShell:**
```powershell
$env:WA_PHONE_ID="your_whatsapp_phone_id_here"
$env:WA_TOKEN="your_permanent_access_token_here"
$env:VERIFY_TOKEN="my_verify_token_here"
```

**Linux / Mac:**
```bash
export WA_PHONE_ID="your_whatsapp_phone_id_here"
export WA_TOKEN="your_permanent_access_token_here"
export VERIFY_TOKEN="my_verify_token_here"
```

---

## 📌 Running Locally

### Development Mode
```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### Run in Background (Windows)
```powershell
Start-Process python app.py
```

Or silently (no console):
```powershell
pythonw app.py
```

---

### Production Mode (Recommended)
Use **Waitress**:

```bash
waitress-serve --listen=127.0.0.1:5000 app:app
```

---

## 📌 Exposing to Internet (Optional)

To connect WhatsApp API, you need a public URL. Use **ngrok**:

1. Install ngrok from: [https://ngrok.com/download](https://ngrok.com/download)  
2. Authenticate ngrok with your account:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```
3. Start tunnel:
   ```bash
   ngrok http 5000
   ```
4. Use the `https://xxxxx.ngrok-free.dev` URL as your webhook in **Meta Developer Console**.

---

## 📌 Example: Sending a Message

From your CRM frontend:
- Enter phone number (with country code, e.g., `919632499491`)
- Type message or generate from prompt
- Click **Send**

---

## 📌 Future Improvements
- Store customer contacts in database (SQLite / MySQL)
- Add conversation history
- AI-powered message generator (using OpenAI API)

---

## 📌 Quick Start Script (Windows)

Create a file `run.bat` inside the project:

```bat
@echo off
echo Starting WhatsApp CRM...
set WA_PHONE_ID=your_whatsapp_phone_id_here
set WA_TOKEN=your_permanent_access_token_here
set VERIFY_TOKEN=my_verify_token_here
python app.py
pause
```

Double-click `run.bat` to launch the CRM.

---
