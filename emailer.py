import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
import config

# 🔧 CONFIG (EDIT THESE)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD
SEND_TO = config.EMAIL_ADDRESS  # You can change this to another email if you want


def send_alert(photo_path, location):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = SEND_TO
    msg["Subject"] = "⚠️ Failed Login Detected"

    body = f"""
Failed login detected!

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Location info:
IP: {location.get('ip')}
City: {location.get('city')}
Region: {location.get('region')}
Country: {location.get('country')}
ISP: {location.get('org')}
"""

    msg.set_content(body)

    # Attach photo
    if photo_path and os.path.exists(photo_path):
        with open(photo_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="image",
                subtype="jpeg",
                filename=os.path.basename(photo_path)
            )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("[📧] Email alert sent")
