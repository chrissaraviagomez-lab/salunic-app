import json
import os
import sys

# Añadir ruta del proyecto para usar la estructura requerida
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from Datos import usuarios
from Datos.datos import cargar_datos, guardar_datos
from Entidades import Usuario
from Funciones.busqueda_lineal import busqueda_lineal_por_email

DB_PATH = os.path.join(os.path.dirname(__file__), "users.json")


def _load_legacy():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def _save_legacy(users):
    try:
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
    except Exception:
        pass


def _sync_from_core_to_legacy():
    try:
        cargar_datos()
    except Exception:
        pass
    users = []
    for u in usuarios:
        users.append({
            "name": getattr(u, 'nombre', ''),
            "email": getattr(u, 'email', ''),
            "password": getattr(u, 'password', ''),
            "id": getattr(u, 'id', None)
        })
    if users:
        _save_legacy(users)


def add_user(name, email, password):
    try:
        cargar_datos()
    except Exception:
        pass
    for u in usuarios:
        if getattr(u, 'email', '').lower() == str(email).lower():
            break
    else:
        new_id = len(usuarios) + 1
        try:
            nuevo = Usuario(id=new_id, nombre=name, email=email, password=password, telefono="+505 00000000")
            usuarios.append(nuevo)
            guardar_datos()
        except Exception:
            pass
    _sync_from_core_to_legacy()
    users = _load_legacy()
    users.append({"name": name, "email": email, "password": password})
    _save_legacy(users)


def find_user(email, password):
    try:
        cargar_datos()
    except Exception:
        pass
    try:
        user_found = busqueda_lineal_por_email(usuarios, email)
        if user_found and getattr(user_found, 'password', None) == password:
            return {
                "name": getattr(user_found, 'nombre', ''),
                "email": getattr(user_found, 'email', ''),
                "password": getattr(user_found, 'password', ''),
                "id": getattr(user_found, 'id', None)
            }
    except Exception:
        pass
    _sync_from_core_to_legacy()
    users = _load_legacy()
    for u in users:
        if str(u.get("email", "")).lower() == str(email).lower() and str(u.get("password", "")) == str(password):
            return u
    return None


def update_user(email_actual, name=None, email_nuevo=None):
    try:
        cargar_datos()
    except Exception:
        pass
    actualizado = False
    for u in usuarios:
        if getattr(u, 'email', '').lower() == str(email_actual).lower():
            if name is not None:
                try:
                    u.nombre = name
                except Exception:
                    pass
            if email_nuevo is not None:
                try:
                    u.email = email_nuevo
                except Exception:
                    pass
            actualizado = True
            break
    if actualizado:
        try:
            guardar_datos()
        except Exception:
            pass
    _sync_from_core_to_legacy()
    if actualizado:
        return True
    users = _load_legacy()
    for u in users:
        if str(u.get("email", "")).lower() == str(email_actual).lower():
            if name is not None:
                u["name"] = name
            if email_nuevo is not None:
                u["email"] = email_nuevo
            actualizado = True
            break
    if actualizado:
        _save_legacy(users)
    return actualizado


def email_exists(email):
    try:
        cargar_datos()
    except Exception:
        pass
    for u in usuarios:
        if getattr(u, 'email', '').lower() == str(email).lower():
            return True
    _sync_from_core_to_legacy()
    users = _load_legacy()
    return any(str(u.get("email", "")).lower() == str(email).lower() for u in users)
