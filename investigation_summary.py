import json
from pathlib import Path
from alert_validator import validate_alert
alerts=json.loads((Path(__file__).parent/"alerts.json").read_text(encoding="utf-8"))
for alert in alerts:
    valid, reason=validate_alert(alert)
    if not valid:
        print(f"REJECTED: {reason}")
        continue
    high=alert["event_id"]==4625 and alert["failed_attempts"]>=10
    print(f"\nINVESTIGATION: {alert['alert_id']}")
    print(f"Account: {alert['username']} | Source: {alert['source_ip']} | Event: {alert['event_id']}")
    print(f"Priority: {'HIGH' if high else 'LOW'}")
    print("Finding: " + ("Reported failed authentication attempts exceeded the configured threshold." if high else "Alert does not exceed the configured threshold."))
    print("Next step: " + ("Correlate 4625 failures with 4624 logons and original event metadata." if high else "Review surrounding activity if additional indicators emerge."))
