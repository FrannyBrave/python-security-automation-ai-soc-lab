import json
from pathlib import Path
from alert_validator import validate_alert
path=Path(__file__).parent/"alerts_invalid.json"
try:
    with path.open(encoding="utf-8") as f: alerts=json.load(f)
    if not isinstance(alerts,list): raise ValueError("Expected a list of alerts")
except (OSError,json.JSONDecodeError,ValueError) as exc:
    print(f"ERROR: Invalid alert input: {exc}")
    raise SystemExit(1)
valid=invalid=0
print("=== SECURITY ALERT VALIDATION ===")
for alert in alerts:
    passed, message=validate_alert(alert)
    valid+=passed
    invalid+=not passed
    aid=alert.get("alert_id","UNKNOWN") if isinstance(alert,dict) else "UNKNOWN"
    print(f"{aid}: {'VALID' if passed else 'INVALID — '+message}")
print(f"Total Alerts: {len(alerts)}\nValid Alerts: {valid}\nInvalid Alerts: {invalid}")
