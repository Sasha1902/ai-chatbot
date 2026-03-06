import json
import os
from datetime import datetime

LOG_FILE = "chat_log.json"

def log_interaction(user_input, bot_response):
    """Speichert jede Chat-Interaktion mit Zeitstempel in einer JSON-Datei."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "bot": bot_response
    }

    # Prüfen, ob Datei existiert
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    # Wieder in Datei schreiben
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)