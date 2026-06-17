import tkinter as tk
from screens.splash_screen import SplashScreen
from screens.inicio_screen import InicioScreen
from screens.home_screen import HomeScreen
from screens.password_reset.screen_1_email import Screen1Email
from screens.password_reset.screen_2_otp import Screen2OTP
from screens.password_reset.screen_3_password import Screen3Password
from screens.forms.form_registro import FormRegistro
from screens.forms.form_cita import FormCita
from screens.forms.form_medicamento import FormMedicamento

class SalunicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salunic - Salud y Bienestar Nicaragua")
        self.root.geometry("375x812")
        self.root.resizable(False, False)
        self.root.config(bg="#ffffff")
        
        # Contenedor principal
        self.container = tk.Frame(root, bg="#ffffff")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Crear todas las pantallas
        for F in (SplashScreen, InicioScreen, HomeScreen, 
                  Screen1Email, Screen2OTP, Screen3Password,
                  FormRegistro, FormCita, FormMedicamento):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Mostrar HomeScreen directamente para cargar el panel profesional
        self.show_frame(HomeScreen)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def main():
    root = tk.Tk()
    app = SalunicApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
