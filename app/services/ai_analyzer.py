import subprocess
import json
import re

def analyze_log(raw_log: str) -> dict:
    prompt = f"""
You are a Senior QA Automation Engineer.

Analyze the following Jenkins TestNG failure log.

Your task:
1. Identify the **exact root cause**
2. Explain **why the failure happened**
3. Suggest **specific code or test fixes**
4. Mention **what to check next if it repeats**

Respond ONLY in JSON.

FORMAT:
{{
  "root_cause": "...",
  "solution": "..."
}}

LOG:
{raw_log}
"""

    try:
        process = subprocess.run(
            ["ollama", "run", "llama3.2:1b"],
            input=prompt.encode(),
            capture_output=True,
            timeout=120
        )

        output = process.stdout.decode("utf-8").strip()
        print("🔍 RAW OLLAMA OUTPUT:\n", output)

        #Extract JSON-like text
        match = re.search(r"\{[\s\S]*", output)
        if not match:
            raise ValueError("No JSON found in AI output")

        json_text = match.group().strip()

        # Auto-fix missing closing brace
        if not json_text.endswith("}"):
            json_text += "}"

        # Parse safely
        data = json.loads(json_text)

        return {
            "root_cause": data.get("root_cause", "Unknown"),
            "solution": data.get("solution", "Unknown")
        }

    except Exception as e:
        print("AI ERROR:", e)
        return {
            "root_cause": "AI analysis failed",
            "solution": str(e)
        }
