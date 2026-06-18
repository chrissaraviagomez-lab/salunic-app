import tkinter as tk
from tkinter import Canvas, messagebox

class RegistroScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.parent = parent
        
        self.canvas = Canvas(
            self,
            width=375,
            height=812,
            bg="#ffffff",
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.nombre_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()
        
        self.create_background()
        self.create_header()
        self.create_form()
        self.create_buttons()
    
    def create_background(self):
        self.canvas.create_rectangle(
            0, 0, 375, 812,
            fill="#f4f6fb",
            outline=""
        )
        
        self.canvas.create_rectangle(
            0, 0, 375, 100,
            fill="#1565c0",
            outline=""
        )
    
    def create_header(self):
        self.canvas.create_text(
            187, 50,
            text="Crear Cuenta",
            font=("Nunito", 28, "bold"),
            fill="#ffffff"
        )
    
    def create_form(self):
        fields = [
            {"label": "Nombre Completo", "var": self.nombre_var, "y": 130},
            {"label": "Email", "var": self.email_var, "y": 220},
            {"label": "Contraseña", "var": self.password_var, "y": 310, "show": "*"},
            {"label": "Confirmar Contraseña", "var": self.confirm_password_var, "y": 400, "show": "*"}
        ]
        
        for field in fields:
            self.canvas.create_text(
                20, field["y"],
                text=field["label"],
                font=("Nunito", 12, "bold"),
                fill="#333333",
                anchor="nw"
            )
            
            entry = tk.Entry(
                self,
                textvariable=field["var"],
                font=("Nunito", 12),
                bg="#ffffff",
                fg="#333333",
                relief=tk.FLAT,
                bd=0,
                show=field.get("show", "")
            )
            self.canvas.create_window(
                187, field["y"] + 40,
                window=entry,
                width=335,
                height=45
            )
            
            self.canvas.create_rectangle(
                20, field["y"] + 30, 355, field["y"] + 75,
                fill="#ffffff",
                outline="#e0e0e0",
                width=1
            )
    
    def create_buttons(self):
        self.registrar_button = self.canvas.create_rectangle(
            20, 530, 355, 580,
            fill="#2ecc71",
            outline=""
        )
        
        self.canvas.create_text(
            187, 555,
            text="Registrarse",
            font=("Nunito", 16, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.tag_bind(self.registrar_button, "<Button-1>", self.on_register)
        
        self.volver_button = self.canvas.create_text(
            187, 620,
            text="¿Ya tienes cuenta? Inicia sesion",
            font=("Nunito", 11),
            fill="#1565c0"
        )
        
        self.canvas.tag_bind(self.volver_button, "<Button-1>", self.on_back_to_login)
    
    def on_register(self, event):
        nombre = self.nombre_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get().strip()
        confirm_password = self.confirm_password_var.get().strip()
        
        if not all([nombre, email, password, confirm_password]):
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        if "@" not in email:
            messagebox.showerror("Error", "Email invalido")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        if email == "usuario@salunic.com":
            messagebox.showerror("Error", "Este email ya esta registrado")
            return
        
        messagebox.showinfo("Exito", "Cuenta creada exitosamente!")
        self.controller.logged_in_user = email
        self.controller.show_screen("Home")
    
    def on_back_to_login(self, event):
        self.controller.show_screen("Login")
