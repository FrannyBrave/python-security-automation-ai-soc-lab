alerts=[
 {"alert_id":"SOC-001","event_id":4625,"failed_attempts":12},
 {"alert_id":"SOC-002","event_id":4625,"failed_attempts":3},
 {"alert_id":"SOC-003","event_id":4625,"failed_attempts":20},
 {"alert_id":"SOC-004","event_id":4624,"failed_attempts":0}
]
print("=== AUTOMATED SECURITY ALERT TRIAGE ===")
for alert in alerts:
    priority="HIGH" if alert["event_id"]==4625 and alert["failed_attempts"]>=10 else "LOW"
    print(f"Alert: {alert['alert_id']} | Event ID: {alert['event_id']} | Failed Attempts: {alert['failed_attempts']} | Priority: {priority}")
