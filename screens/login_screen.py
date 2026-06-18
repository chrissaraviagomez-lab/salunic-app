import tkinter as tk
from tkinter import Canvas, messagebox

class LoginScreen(tk.Frame):
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
        
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        self.create_background()
        self.create_header()
        self.create_form()
        self.create_buttons()
        self.create_footer()
    
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
            text="Iniciar Sesion",
            font=("Nunito", 28, "bold"),
            fill="#ffffff"
        )
    
    def create_form(self):
        self.canvas.create_text(
            20, 150,
            text="Email",
            font=("Nunito", 12, "bold"),
            fill="#333333",
            anchor="nw"
        )
        
        self.email_entry = tk.Entry(
            self,
            textvariable=self.email_var,
            font=("Nunito", 12),
            bg="#ffffff",
            fg="#333333",
            relief=tk.FLAT,
            bd=0
        )
        self.canvas.create_window(
            187, 190,
            window=self.email_entry,
            width=335,
            height=45
        )
        
        self.canvas.create_rectangle(
            20, 180, 355, 225,
            fill="#ffffff",
            outline="#e0e0e0",
            width=1
        )
        
        self.canvas.create_text(
            20, 260,
            text="Contraseña",
            font=("Nunito", 12, "bold"),
            fill="#333333",
            anchor="nw"
        )
        
        self.password_entry = tk.Entry(
            self,
            textvariable=self.password_var,
            font=("Nunito", 12),
            bg="#ffffff",
            fg="#333333",
            relief=tk.FLAT,
            bd=0,
            show="*"
        )
        self.canvas.create_window(
            187, 300,
            window=self.password_entry,
            width=335,
            height=45
        )
        
        self.canvas.create_rectangle(
            20, 290, 355, 335,
            fill="#ffffff",
            outline="#e0e0e0",
            width=1
        )
    
    def create_buttons(self):
        self.login_button = self.canvas.create_rectangle(
            20, 380, 355, 430,
            fill="#1565c0",
            outline=""
        )
        
        self.canvas.create_text(
            187, 405,
            text="Iniciar Sesion",
            font=("Nunito", 16, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.tag_bind(self.login_button, "<Button-1>", self.on_login)
        
        self.olvide_button = self.canvas.create_text(
            187, 460,
            text="¿Olvidaste tu contraseña?",
            font=("Nunito", 11),
            fill="#1565c0"
        )
        
        self.canvas.tag_bind(self.olvide_button, "<Button-1>", self.on_forgot_password)
    
    def create_footer(self):
        self.canvas.create_text(
            187, 530,
            text="¿No tienes cuenta?",
            font=("Nunito", 12),
            fill="#333333"
        )
        
        self.registro_button = self.canvas.create_text(
            187, 560,
            text="Registrate aqui",
            font=("Nunito", 12, "bold"),
            fill="#2ecc71"
        )
        
        self.canvas.tag_bind(self.registro_button, "<Button-1>", self.on_register)
    
    def on_login(self, event):
        email = self.email_var.get().strip()
        password = self.password_var.get().strip()
        
        if not email or not password:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        if email == "usuario@salunic.com" and password == "123456":
            self.controller.logged_in_user = email
            self.controller.show_screen("Home")
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")
            self.password_var.set("")
    
    def on_forgot_password(self, event):
        messagebox.showinfo("Recuperar Contraseña", "Contacta a soporte@salunic.com para recuperar tu contraseña")
    
    def on_register(self, event):
        self.controller.show_screen("Registro")
