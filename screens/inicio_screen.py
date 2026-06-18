import tkinter as tk

class InicioScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        
        # Fondo blanco
        self.create_widgets()
    
    def create_widgets(self):
        # Encabezado azul
        header = tk.Frame(self, bg="#1565c0", height=150)
        header.pack(fill="x")
        
        title = tk.Label(
            header,
            text="Bienvenido a SALUNIC",
            font=("Nunito", 24, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        title.pack(pady=40)
        
        subtitle = tk.Label(
            header,
            text="Tu plataforma de salud y bienestar",
            font=("Nunito", 12),
            fg="#e0e0e0",
            bg="#1565c0"
        )
        subtitle.pack()
        
        # Contenido
        content = tk.Frame(self, bg="#ffffff")
        content.pack(fill="both", expand=True, padx=20, pady=40)
        
        description = tk.Label(
            content,
            text="Accede a tu cuenta para comenzar a cuidar tu salud.",
            font=("Nunito", 14),
            fg="#555555",
            bg="#ffffff",
            wraplength=300,
            justify="center"
        )
        description.pack(pady=30)
        
        # Botones
        btn_comenzar = tk.Button(
            content,
            text="Comenzar",
            font=("Nunito", 14, "bold"),
            bg="#2ecc71",
            fg="#ffffff",
            width=20,
            command=lambda: self.controller.show_screen("Login")
        )
        btn_comenzar.pack(pady=15)
        
        btn_login = tk.Button(
            content,
            text="Iniciar Sesión",
            font=("Nunito", 14, "bold"),
            bg="#3498db",
            fg="#ffffff",
            width=20,
            command=lambda: self.controller.show_screen("Login")
        )
        btn_login.pack(pady=15)
