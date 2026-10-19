import json
from pathlib import Path
with (Path(__file__).parent/"alerts.json").open(encoding="utf-8") as f:
    alerts=json.load(f)
high=low=0
print("=== JSON SECURITY ALERT TRIAGE ===")
for alert in alerts:
    priority="HIGH" if alert["event_id"]==4625 and alert["failed_attempts"]>=10 else "LOW"
    high+=priority=="HIGH"
    low+=priority=="LOW"
    print(f"{alert['alert_id']} | Account: {alert['username']} | Failed Attempts: {alert['failed_attempts']} | Priority: {priority}")
print(f"Total Alerts: {len(alerts)}\nHigh Priority: {high}\nLow Priority: {low}")
