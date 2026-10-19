# Python Security Alert Automation & AI-Assisted SOC Investigation

Hands-on Python cybersecurity lab using **synthetic Windows authentication alerts**. It demonstrates deterministic triage, JSON data validation, CSV/JSON reporting, and optional AI-assisted investigation briefs through the OpenAI API. This is a **training environment**, not a live SIEM or confirmed incident response operation.

## Architecture

```text
Synthetic Windows alerts (alerts.json)
    → validate_alert()
    → rule-based triage (Event ID 4625 and ≥10 failures = HIGH)
    → CSV and JSON reports
    → optional OpenAI API investigation summaries
    → PENDING_ANALYST_REVIEW
```

## Features

- JSON input validation with rejected-record reporting and malformed-file error handling
- Rule-based HIGH/LOW prioritization for simulated failed logons
- CSV triage exports and structured JSON investigations
- Unit tests for six validation cases
- AI summaries that distinguish evidence from hypotheses and preserve rule-based priority
- Incomplete-response detection and bounded AI request counts
- Local API token usage logging; no automatic containment actions

## Run locally

Requires Python 3 and optional OpenAI API credentials for AI exercises.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -v
python secure_triage_pipeline.py
python export_investigations.py
```

Optional: create a private `.env` from `.env.example` and set `OPENAI_API_KEY` before running `ai_investigation.py` or `multi_ai_investigation.py`. AI requests may incur charges. Never publish `.env`.

## Evidence and limitations

The lab includes synthetic data only; documentation-only IP addresses are not threat-intelligence evidence. The simple detection rule is not production validated. AI-generated hypotheses require corroborating telemetry and analyst review before any response action. The training demonstrated six passing validator tests and structured reporting.

Selected synthetic example reports are provided as text and CSV files. The original screenshot evidence is preserved in the separately prepared downloadable Lab 3 portfolio ZIP; screenshots have not yet been uploaded to this GitHub repository.

**Repository publication note:** This GitHub version was rebuilt through the connected GitHub account after local HTTPS push authentication failed. It contains equivalent working exercises but is not an identical commit-by-commit mirror of the original Mac repository. The local and remote Git histories are separate; do not force-push one over the other.
