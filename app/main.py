import tkinter as tk
from screens.splash_screen import SplashScreen
from screens.inicio_screen import InicioScreen
from screens.login_screen import LoginScreen
from screens.registro_screen import RegistroScreen
from screens.home_screen import HomeScreen
from screens.citas_screen import CitasScreen
from screens.historial_screen import HistorialScreen
from screens.medicamentos_screen import MedicamentosScreen
from screens.estadisticas_screen import EstadisticasScreen
from screens.forms.form_medicamento import FormMedicamento
from screens.forms.form_registro import FormRegistro
from screens.password_reset.screen_2_otp import Screen2OTP

class SalunicApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("SALUNIC - Salud y Bienestar")
        self.geometry("375x812")
        self.resizable(False, False)
        
        self.current_user = None
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.container = container
        
        self.show_screen("Splash")
    
    def show_screen(self, name):
        if name in self.frames:
            frame = self.frames[name]
            frame.tkraise()
        else:
            if name == "Splash":
                frame = SplashScreen(self.container, self)
            elif name == "Inicio":
                frame = InicioScreen(self.container, self)
            elif name == "Login":
                frame = LoginScreen(self.container, self)
            elif name == "Registro":
                frame = RegistroScreen(self.container, self)
            elif name == "Home":
                frame = HomeScreen(self.container, self)
            elif name == "Citas":
                frame = CitasScreen(self.container, self)
            elif name == "Historial":
                frame = HistorialScreen(self.container, self)
            elif name == "Medicamentos":
                frame = MedicamentosScreen(self.container, self)
            elif name == "Estadisticas":
                frame = EstadisticasScreen(self.container, self)
            elif name == "FormMedicamento":
                frame = FormMedicamento(self.container, self)
            elif name == "FormRegistro":
                frame = FormRegistro(self.container, self)
            elif name == "Screen2OTP":
                frame = Screen2OTP(self.container, self)
            
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

if __name__ == "__main__":
    app = SalunicApp()
    app.mainloop()
