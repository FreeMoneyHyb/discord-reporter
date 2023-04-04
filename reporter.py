import requests
import time

chanelid = input("[?] Enter A Channel Id: ")
messageid = input("[?] Enter A Message Id: ")
token = input("[?] Enter An Account Token: ")

for i in range(99999999):
    url = "https://discord.com/api/v9/reporting/message"
    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    payload = {
        "version": "1.0",
        "variant": "3",
        "language": "en",
        "breadcrumbs": [3, 31],
        "name": "message",
        "channel_id": chanelid,
        "message_id": messageid,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        report_id = response.json().get("report_id")
        print(f"[{i}] Report ID: {report_id}")
    except Exception as e:
        print(f"[{i}] ERROR: {e}")

    time.sleep(0.5)
