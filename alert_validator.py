REQUIRED_FIELDS = ["alert_id", "event_id", "username", "failed_attempts", "source_ip"]

def validate_alert(alert):
    if not isinstance(alert, dict):
        return False, "Alert must be an object"
    missing = [field for field in REQUIRED_FIELDS if field not in alert]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    if not isinstance(alert["event_id"], int) or isinstance(alert["event_id"], bool):
        return False, "event_id must be an integer"
    n = alert["failed_attempts"]
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        return False, "failed_attempts must be a non-negative integer"
    return True, "Valid alert"
