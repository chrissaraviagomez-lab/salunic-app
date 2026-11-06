import sys
import os

ROOT = r"C:\salunic-app"
APP = os.path.join(ROOT, "app")
for p in (ROOT, APP):
    if p not in sys.path:
        sys.path.insert(0, p)

import tkinter as tk
from PIL import ImageGrab

# Cargar datos y preparar estado para capturas útiles
try:
    from Funciones import sistema
    from Funciones.cola_atencion import cola_atencion
    sistema.iniciar_sistema()
    # Sembrar cola para que la captura del Panel de Atención muestre prioridad
    cola_atencion.cola.clear()
    cola_atencion.turno_global = 0
    cola_atencion.encolar({"paciente": "Ana Perez", "cita_id": 101, "hora": "08:30"}, es_adulto_mayor=False)
    cola_atencion.encolar({"paciente": "Jose Martinez (Adulto Mayor)", "cita_id": 102, "hora": "09:00"}, es_adulto_mayor=True)
    cola_atencion.encolar({"paciente": "Luis Gomez", "cita_id": 103, "hora": "09:30"}, es_adulto_mayor=False)
except Exception as e:
    print("Aviso preparando datos:", e)

root = tk.Tk()
root.geometry("375x812")
root.update_idletasks()

class Controller:
    def __init__(self):
        self.current_user = {"name": "Maria Gonzalez", "email": "maria.gonzalez@salunic.com", "id": 1}
    def show_screen(self, name):
        pass

ctrl = Controller()

from screens.splash_screen import SplashScreen
from screens.inicio_screen import InicioScreen
from screens.login_screen import LoginScreen
from screens.registro_screen import RegistroScreen
from screens.home_screen import HomeScreen
from screens.citas_screen import CitasScreen
from screens.atencion_screen import AtencionScreen
from screens.historial_screen import HistorialScreen
from screens.medicamentos_screen import MedicamentosScreen
from screens.estadisticas_screen import EstadisticasScreen
from screens.forms.form_medicamento import FormMedicamento
from screens.forms.form_registro import FormRegistro

out = os.path.join(ROOT, "docs", "capturas")
os.makedirs(out, exist_ok=True)

shots = [
    ("01_inicio_login", InicioScreen),
    ("02_login", LoginScreen),
    ("03_registro", RegistroScreen),
    ("04_home", HomeScreen),
    ("05_citas", CitasScreen),
    ("06_panel_atencion_prioridad", AtencionScreen),
    ("07_medicamentos", MedicamentosScreen),
]

for name, cls in shots:
    try:
        # refrescar instancia de controller por si acaso
        c = Controller()
        s = cls(root, c)
        s.pack(fill="both", expand=True)
        root.update_idletasks()
        root.update()
        root.deiconify()
        root.lift()
        root.attributes('-topmost', True)
        root.after(150, lambda: None)
        root.update()
        x = root.winfo_rootx(); y = root.winfo_rooty()
        w = root.winfo_width(); h = root.winfo_height()
        if w > 1 and h > 1:
            img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
            path = os.path.join(out, name + ".png")
            img.save(path)
            print("Guardado:", path)
        else:
            print("Tamano invalido para", name)
        s.destroy()
        root.update()
    except Exception as e:
        print("Error en", name, ":", e)

root.destroy()
print("DONE. Capturas en:", out)
print("NOTA: Las capturas de CONSOLA (menu y cola con prioridad/JSON) deben tomarse manualmente con Win+Shift+S o Recortes al ejecutar: py consola/main.py")
