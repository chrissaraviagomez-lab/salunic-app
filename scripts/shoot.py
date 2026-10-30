import sys; sys.path.insert(0, "C:/salunic-app")
import tkinter as tk
from PIL import ImageGrab
import os

root = tk.Tk(); root.geometry("375x812")
root.update_idletasks()
ctrl = type("obj", (object,), {"current_user": None, "show_screen": lambda n: None})()

from screens.inicio_screen import InicioScreen
from screens.login_screen import LoginScreen
from screens.registro_screen import RegistroScreen
from screens.home_screen import HomeScreen
from screens.citas_screen import CitasScreen
from screens.historial_screen import HistorialScreen
from screens.forms.form_medicamento import FormMedicamento
from screens.forms.form_registro import FormRegistro
from screens.password_reset.screen_2_otp import Screen2OTP
from screens.splash_screen import SplashScreen

out = "C:/Users/cristian.saravia/AppData/Local/Temp/opencode/shots"
os.makedirs(out, exist_ok=True)

for name, cls in [("01_splash",SplashScreen),("02_inicio",InicioScreen),("03_login",LoginScreen),
                  ("04_registro",RegistroScreen),("05_home",HomeScreen),("06_citas",CitasScreen),
                  ("07_historial",HistorialScreen),("08_formmed",FormMedicamento),
                  ("09_formreg",FormRegistro),("10_otp",Screen2OTP)]:
    s = cls(root, ctrl)
    s.pack(fill="both", expand=True)
    root.update_idletasks()
    root.update()
    root.lift()
    x = root.winfo_rootx(); y = root.winfo_rooty()
    w = root.winfo_width(); h = root.winfo_height()
    img = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    img.save(os.path.join(out, name + ".png"))
    print("Guardado:", name)
    s.destroy()

root.destroy()
print("DONE")
