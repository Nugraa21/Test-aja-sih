import json, os, getpass

USER_FILE = "storage/users.json"

def load_users(default):
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump(default, f, indent=4)
    with open(USER_FILE) as f:
        return json.load(f)

def login(users):
    u = input("User: ")
    p = getpass.getpass("Password: ")
    if u in users and users[u]["password"] == p:
        return u, users[u]["role"]
    print("Login gagal")
    return None, None
