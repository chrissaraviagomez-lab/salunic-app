import tkinter as tk
from tkinter import messagebox

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Encabezado
        header = tk.Frame(self, bg="#1565c0", height=100)
        header.pack(fill="x")
        
        title = tk.Label(
            header,
            text="Iniciar Sesión",
            font=("Nunito", 24, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        title.pack(pady=30)
        
        # Contenido
        content = tk.Frame(self, bg="#ffffff")
        content.pack(fill="both", expand=True, padx=20, pady=30)
        
        # Email
        tk.Label(
            content,
            text="Email:",
            font=("Nunito", 12),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", pady=(10, 5))
        
        self.email_entry = tk.Entry(
            content,
            font=("Nunito", 12),
            width=30,
            bg="#f5f5f5"
        )
        self.email_entry.pack(fill="x", pady=(0, 15))
        self.email_entry.insert(0, "usuario@salunic.com")
        
        # Contraseña
        tk.Label(
            content,
            text="Contraseña:",
            font=("Nunito", 12),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", pady=(10, 5))
        
        self.password_entry = tk.Entry(
            content,
            font=("Nunito", 12),
            width=30,
            bg="#f5f5f5",
            show="*"
        )
        self.password_entry.pack(fill="x", pady=(0, 15))
        self.password_entry.insert(0, "123456")
        
        # Botón Iniciar
        btn_login = tk.Button(
            content,
            text="Iniciar Sesión",
            font=("Nunito", 14, "bold"),
            bg="#1565c0",
            fg="#ffffff",
            command=self.login
        )
        btn_login.pack(fill="x", pady=20)
        
        # Enlace a Registro
        btn_register = tk.Button(
            content,
            text="¿No tienes cuenta? Regístrate",
            font=("Nunito", 11),
            bg="#ffffff",
            fg="#3498db",
            relief="flat",
            command=lambda: self.controller.show_screen("Registro")
        )
        btn_register.pack(pady=10)
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if email and password:
            self.controller.logged_in_user = email
            self.controller.show_screen("Home")
        else:
            messagebox.showerror("Error", "Por favor completa todos los campos")
