"""Optional manual OpenAI connection check; incurs API charges when run."""
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
def main():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY missing")
        return 1
    try:
        response=OpenAI(timeout=30.0,max_retries=0).responses.create(
            model="gpt-5-mini",
            instructions="Be concise and accurate about cybersecurity.",
            input="In one sentence explain Windows Event ID 4625.",
            max_output_tokens=150)
        print(response.output_text)
        return 0
    except OpenAIError as exc:
        print(f"ERROR: {type(exc).__name__}")
        return 1
if __name__=="__main__":
    raise SystemExit(main())
