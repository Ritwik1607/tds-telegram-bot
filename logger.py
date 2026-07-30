import json
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "run.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)


class AgentLogger:

    def log(self, event_type: str, data: dict):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event_type,
            "data": data
        }

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def get_log_path(self):
        return LOG_FILE


logger = AgentLogger()