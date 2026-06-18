import tkinter as tk
from tkinter import Canvas


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f4f6fb")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#f4f6fb", highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 375, 812, fill="#f4f6fb", outline="")
        self.canvas.create_rectangle(0, 0, 375, 210, fill="#1565c0", outline="")
        self.canvas.create_text(28, 78, text="Iniciar Sesion", font=("Nunito", 24, "bold"), fill="#ffffff", anchor="w")
        self.canvas.create_text(
            28,
            118,
            text="Accede con email o usuario para continuar en Salunic.",
            font=("Nunito", 12),
            fill="#ffffff",
            anchor="w",
            width=320,
        )

        self.canvas.create_text(28, 256, text="Email o Usuario", font=("Nunito", 12, "bold"), fill="#1565c0", anchor="w")
        self.usuario_entry = tk.Entry(self, font=("Nunito", 13), bd=0, bg="#ffffff", fg="#1f2a44")
        self.canvas.create_window(187, 292, window=self.usuario_entry, width=319, height=42)

        self.canvas.create_text(28, 334, text="Contrasena", font=("Nunito", 12, "bold"), fill="#1565c0", anchor="w")
        self.password_entry = tk.Entry(self, font=("Nunito", 13), bd=0, bg="#ffffff", fg="#1f2a44", show="*")
        self.canvas.create_window(187, 370, window=self.password_entry, width=319, height=42)

        self.canvas.create_text(28, 412, text="Recuperar contrasena", font=("Nunito", 11, "bold"), fill="#e91e8c", anchor="w")

        entrar_btn = tk.Button(
            self,
            text="Entrar",
            font=("Nunito", 14, "bold"),
            bg="#2ecc71",
            fg="#ffffff",
            activebackground="#2ecc71",
            activeforeground="#ffffff",
            bd=0,
            command=lambda: self.controller.show_screen("FormRegistro"),
        )
        self.canvas.create_window(187, 478, window=entrar_btn, width=319, height=48)

        registro_btn = tk.Button(
            self,
            text="Registrarse",
            font=("Nunito", 14, "bold"),
            bg="#ffffff",
            fg="#1565c0",
            activebackground="#ffffff",
            activeforeground="#1565c0",
            bd=1,
            command=lambda: self.controller.show_screen("FormRegistro"),
        )
        self.canvas.create_window(187, 540, window=registro_btn, width=319, height=48)
