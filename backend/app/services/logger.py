import json
from pathlib import Path
from datetime import datetime
from app.config import LOG_FILE_PATH

LOG_FILE = Path(LOG_FILE_PATH)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_interaction(user_id, prompt, response, mode):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "mode": mode,
        "prompt": prompt,
        "response": response
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
