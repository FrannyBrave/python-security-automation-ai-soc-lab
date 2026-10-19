import json
from pathlib import Path
from alert_validator import validate_alert

root = Path(__file__).parent
try:
    with (root / "alerts.json").open(encoding="utf-8") as f:
        alerts = json.load(f)
    if not isinstance(alerts, list):
        raise ValueError("Expected a list of alerts")
except (OSError, ValueError, json.JSONDecodeError) as exc:
    print(f"ERROR: Unable to load alerts: {exc}")
    raise SystemExit(1)

results = []
for alert in alerts:
    valid, reason = validate_alert(alert)
    if not valid:
        print(f"REJECTED: {reason}")
        continue
    if alert["event_id"] == 4625 and alert["failed_attempts"] >= 10:
        priority, finding, recommendation = "HIGH","Failed logons exceeded the configured threshold.","Investigate source and subsequent account activity."
    elif alert["event_id"] == 4625:
        priority, finding, recommendation = "LOW","Failed logons remained below the configured threshold.","Monitor for additional authentication failures."
    else:
        priority, finding, recommendation = "LOW","Event did not match the failed-logon rule.","Review if other suspicious indicators exist."
    results.append({"alert_id":alert["alert_id"],"account":alert["username"],"source_ip":alert["source_ip"],
                    "event_id":alert["event_id"],"failed_attempts":alert["failed_attempts"],
                    "priority":priority,"finding":finding,"recommendation":recommendation,
                    "review_status":"PENDING_ANALYST_REVIEW"})
with (root / "investigation_results.json").open("w",encoding="utf-8") as f:
    json.dump(results,f,indent=2)
print(f"Investigations generated: {len(results)}")
print("Output file: investigation_results.json")
