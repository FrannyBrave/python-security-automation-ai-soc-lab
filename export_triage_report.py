import csv
import json
from pathlib import Path
root=Path(__file__).parent
alerts=json.loads((root/"alerts.json").read_text(encoding="utf-8"))
fields=["Alert ID","Event ID","Account","Source IP","Failed Attempts","Priority","Recommendation"]
records=[]
for alert in alerts:
    high=alert["event_id"]==4625 and alert["failed_attempts"]>=10
    records.append({"Alert ID":alert["alert_id"],"Event ID":alert["event_id"],"Account":alert["username"],"Source IP":alert["source_ip"],"Failed Attempts":alert["failed_attempts"],"Priority":"HIGH" if high else "LOW","Recommendation":"Investigate repeated authentication failures" if high else "Review if context warrants investigation"})
with (root/"triage_report.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)
print(f"Alerts processed: {len(records)}")
print("Report saved to: triage_report.csv")
