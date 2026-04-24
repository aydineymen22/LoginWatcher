import subprocess
import time
import json

from camera import take_photo
from location import get_location
from emailer import send_alert

POLL_INTERVAL = 2   
EVENT_ID = 4625

last_record_id = None


def get_latest_failed_login():
    ps_cmd = f"""
    Get-WinEvent -FilterHashtable @{{
        LogName='Security';
        Id={EVENT_ID}
    }} -MaxEvents 1 |
    Select-Object RecordId |
    ConvertTo-Json
    """

    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        capture_output=True,
        text=True
    )

    if not result.stdout.strip():
        return None

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def check_failed_login():
    global last_record_id

    event = get_latest_failed_login()
    if not event:
        return

    record_id = event["RecordId"]

    if last_record_id is None:
        last_record_id = record_id
        print("[*] Baseline set. Monitoring new failed logins.")
        return

    if record_id <= last_record_id:
        return

    last_record_id = record_id
    print("[!] New failed login detected")

    photo_path = take_photo()
    location = get_location()
    send_alert(photo_path, location)


def main():
    print("[*] LoginWatcher started")
    print("[*] Monitoring failed logins (Event ID 4625)...")

    while True:
        check_failed_login()
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
