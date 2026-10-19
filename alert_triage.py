alert={"alert_id":"SOC-001","event_id":4625,"username":"alex.morgan","failed_attempts":12,"source_ip":"203.0.113.25","time_window_minutes":5}
print("=== SECURITY ALERT TRIAGE ===")
for key,value in alert.items():
    print(f"{key}: {value}")
if alert["event_id"]==4625 and alert["failed_attempts"]>=10:
    print("Priority: HIGH")
    print("Reason: Multiple failed authentication attempts detected.")
    print("Recommended action: Investigate account and source IP.")
else:
    print("Priority: LOW")
    print("Reason: Alert does not meet the current investigation threshold.")
