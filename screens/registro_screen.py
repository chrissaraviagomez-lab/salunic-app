import tkinter as tk
from tkinter import messagebox

class RegistroScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Encabezado
        header = tk.Frame(self, bg="#1565c0", height=80)
        header.pack(fill="x")
        
        title = tk.Label(
            header,
            text="Crear Cuenta",
            font=("Nunito", 24, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        title.pack(pady=20)
        
        # Contenido scrollable
        canvas = tk.Canvas(self, bg="#ffffff", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#ffffff")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Campos del formulario
        self.create_form_fields(scrollable_frame)
    
    def create_form_fields(self, parent):
        # Nombre
        tk.Label(
            parent,
            text="Nombre Completo:",
            font=("Nunito", 11),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(20, 5))
        
        self.name_entry = tk.Entry(
            parent,
            font=("Nunito", 11),
            width=30,
            bg="#f5f5f5"
        )
        self.name_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Email
        tk.Label(
            parent,
            text="Email:",
            font=("Nunito", 11),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.email_entry = tk.Entry(
            parent,
            font=("Nunito", 11),
            width=30,
            bg="#f5f5f5"
        )
        self.email_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Contraseña
        tk.Label(
            parent,
            text="Contraseña:",
            font=("Nunito", 11),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.password_entry = tk.Entry(
            parent,
            font=("Nunito", 11),
            width=30,
            bg="#f5f5f5",
            show="*"
        )
        self.password_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Confirmar Contraseña
        tk.Label(
            parent,
            text="Confirmar Contraseña:",
            font=("Nunito", 11),
            fg="#333333",
            bg="#ffffff"
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.confirm_password_entry = tk.Entry(
            parent,
            font=("Nunito", 11),
            width=30,
            bg="#f5f5f5",
            show="*"
        )
        self.confirm_password_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Botón Registrar
        btn_register = tk.Button(
            parent,
            text="Crear Cuenta",
            font=("Nunito", 12, "bold"),
            bg="#2ecc71",
            fg="#ffffff",
            command=self.register
        )
        btn_register.pack(fill="x", padx=20, pady=20)
        
        # Botón Volver
        btn_back = tk.Button(
            parent,
            text="Volver",
            font=("Nunito", 11),
            bg="#ffffff",
            fg="#1565c0",
            relief="flat",
            command=lambda: self.controller.show_screen("Inicio")
        )
        btn_back.pack(fill="x", padx=20, pady=(0, 20))
    
    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if not all([name, email, password, confirm_password]):
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
            return
        
        self.controller.logged_in_user = email
        messagebox.showinfo("Éxito", "Cuenta creada correctamente")
        self.controller.show_screen("Home")
