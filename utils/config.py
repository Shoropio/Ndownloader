import json
import os

CONFIG_FILE = "settings.json"
HISTORY_FILE = "history.json"

DEFAULT_CONFIG = {
    "output_path": os.path.join(os.path.expanduser("~"), "Downloads"),
    "theme": "dark",
    "language": "es",
    "last_format": "Video (MP4)",
    "last_quality": "Best Quality"
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def add_to_history(entry):
    history = load_history()
    history.insert(0, entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[:50], f, indent=4) # Keep last 50
