import json, os

BASE = "storage"
FS_FILE = f"{BASE}/fs.json"

def load_fs(default):
    if not os.path.exists(FS_FILE):
        with open(FS_FILE, "w") as f:
            json.dump(default, f, indent=4)
    with open(FS_FILE) as f:
        return json.load(f)

def save_fs(fs):
    with open(FS_FILE, "w") as f:
        json.dump(fs, f, indent=4)
