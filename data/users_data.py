import json, os

DB_PATH = os.path.join(os.path.dirname(__file__), "users.json")

def _load():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _save(users):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def add_user(name, email, password):
    users = _load()
    users.append({"name": name, "email": email, "password": password})
    _save(users)

def find_user(email, password):
    users = _load()
    for u in users:
        if u["email"] == email and u["password"] == password:
            return u
    return None

def update_user(email_actual, name=None, email_nuevo=None):
    users = _load()
    actualizado = False
    for u in users:
        if u["email"] == email_actual:
            if name is not None:
                u["name"] = name
            if email_nuevo is not None:
                u["email"] = email_nuevo
            actualizado = True
            break
    if actualizado:
        _save(users)
    return actualizado

def email_exists(email):
    users = _load()
    return any(u["email"] == email for u in users)
