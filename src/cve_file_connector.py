import json
from fastapi import HTTPException

FILE = "./src/CVEs_file/known_exploited_vulnerabilities.json"

def LoadCvesFile():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            cveDump = f.read()
        return json.loads(cveDump)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")