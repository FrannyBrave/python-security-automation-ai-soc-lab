import csv
from datetime import datetime, timezone
from pathlib import Path

def log_api_usage(alert_id, response):
    if not response.usage:
        return
    usage_file = Path(__file__).parent / "api_usage_log.csv"
    existed = usage_file.exists()
    with usage_file.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not existed:
            writer.writerow(["timestamp_utc","alert_id","model","input_tokens","output_tokens"])
        writer.writerow([datetime.now(timezone.utc).isoformat(),alert_id,response.model,response.usage.input_tokens,response.usage.output_tokens])
