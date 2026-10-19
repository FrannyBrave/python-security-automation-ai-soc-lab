import csv
import json
from pathlib import Path
from alert_validator import validate_alert

root = Path(__file__).parent
try:
    with (root / "alerts_invalid.json").open(encoding="utf-8") as f:
        alerts = json.load(f)
    if not isinstance(alerts, list):
        raise ValueError("Expected a list of alerts")
except (OSError, ValueError, json.JSONDecodeError) as exc:
    print(f"ERROR: Unable to read alerts: {exc}")
    raise SystemExit(1)

valid_results = []
rejected = 0
for alert in alerts:
    valid, reason = validate_alert(alert)
    if not valid:
        rejected += 1
        aid = alert.get("alert_id", "UNKNOWN") if isinstance(alert, dict) else "UNKNOWN"
        print(f"REJECTED: {aid} — {reason}")
        continue
    high = alert["event_id"] == 4625 and alert["failed_attempts"] >= 10
    valid_results.append({
        "Alert ID": alert["alert_id"],
        "Event ID": alert["event_id"],
        "Account": alert["username"],
        "Source IP": alert["source_ip"],
        "Failed Attempts": alert["failed_attempts"],
        "Priority": "HIGH" if high else "LOW",
        "Recommendation": "Investigate repeated authentication failures" if high else "Review context if needed"
    })

fields = ["Alert ID","Event ID","Account","Source IP","Failed Attempts","Priority","Recommendation"]
try:
    with (root / "validated_triage_report.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(valid_results)
except OSError as exc:
    print(f"ERROR: Unable to write report: {exc}")
    raise SystemExit(1)

print("=== SECURITY TRIAGE PIPELINE SUMMARY ===")
print(f"Total Alerts: {len(alerts)}")
print(f"Valid Alerts: {len(valid_results)}")
print(f"Rejected Alerts: {rejected}")
print(f"HIGH Priority: {sum(r['Priority']=='HIGH' for r in valid_results)}")
print(f"LOW Priority: {sum(r['Priority']=='LOW' for r in valid_results)}")
print("Report saved to: validated_triage_report.csv")
