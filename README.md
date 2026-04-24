# LoginWatcher

**Stealth Forensic Capture & Alert System for Windows**

LoginWatcher is a Python-based security agent designed to protect your laptop in the event of physical theft. It monitors the Windows Security Event Log for failed login attempts. When an intruder enters an incorrect password at the lock screen, the agent silently captures a photo using the webcam, identifies the device's geographical location, and sends an email alert with the photo to the owner.

## 🚀 Key Features

* **Real-time Monitoring**: Automatically detects failed authentication attempts (Windows Event ID 4625).
* **Stealth Photo Capture**: Silently activates the webcam to snap a photo of the intruder.
* **Geolocation Forensics**: Retrieves the public IP, city, region, and ISP data of the intruder.
* **Automatic Email Alerts**: Sends a detailed report including the intruder's photo directly to your inbox.
* **Pre-Login Persistence**: Runs as a high-privilege system task that starts before any user logs in.

## 🛠️ Installation & Setup

### 1. Prerequisites
You will need Python 3.12+ installed. Install the required libraries:
```bash
pip install opencv-python requests
```

### 2. Project Location
For maximum reliability and to avoid OneDrive sync issues, move all project files to:
C:\LoginWatcher\

### 3. Configuration
Create a file named config.py in the project folder to store your email credentials:

### config.py
EMAIL_ADDRESS = "your-email@gmail.com" 

EMAIL_PASSWORD = "your-gmail-app-password" 

Note: Use a Gmail "App Password," not your regular password.


## 🛡️ Windows Deployment
To catch a thief at the lock screen, this script must be run as a Windows Scheduled Task:

Trigger: Set to "At startup".

User Account: Select "Run whether user is logged on or not".

Privileges: Check "Run with highest privileges".

Action: Point to your python.exe and the script login_watcher.py.

Start In: Set the working directory to C:\LoginWatcher\.

## 📁 Project Structure
login_watcher.py: The main service that polls for Event ID 4625.

camera.py: Optimised script for rapid, stealthy photo capture.

emailer.py: Handles SMTP communication and photo attachments.

location.py: Fetches network-based location data via ipinfo.io.

## ⚖️ Disclaimer
This project is intended for personal security and educational purposes only. Always ensure your use of surveillance technology complies with local laws and regulations.
