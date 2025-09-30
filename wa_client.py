import os
import requests

class WAClient:
    def __init__(self):
        self.phone_id = os.getenv("WA_PHONE_ID")
        self.token = os.getenv("WA_TOKEN")
        self.url = f"https://graph.facebook.com/v18.0/{self.phone_id}/messages"

    def send_text(self, to, text):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": to,  # phone number in international format e.g. "919632499491"
            "type": "text",
            "text": {"body": text}
        }
        response = requests.post(self.url, headers=headers, json=payload)
        return response.json()
