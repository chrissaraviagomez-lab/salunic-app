import tkinter as tk
from tkinter import Canvas


class FormRegistro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f4f6fb")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#f4f6fb", highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 375, 812, fill="#f4f6fb", outline="")
        self.canvas.create_rectangle(0, 0, 375, 210, fill="#1565c0", outline="")
        self.canvas.create_text(28, 78, text="Crear Cuenta", font=("Nunito", 24, "bold"), fill="#ffffff", anchor="w")
        self.canvas.create_text(
            28,
            118,
            text="Completa tus datos personales para registrarte en Salunic.",
            font=("Nunito", 12),
            fill="#ffffff",
            anchor="w",
            width=320,
        )

        labels = [
            ("Nombre Completo", 256),
            ("Email", 334),
            ("Contrasena", 412),
            ("Confirmar Contrasena", 490),
        ]
        self.entries = {}
        for label, y in labels:
            self.canvas.create_text(28, y, text=label, font=("Nunito", 12, "bold"), fill="#1565c0", anchor="w")
            show_char = "*" if "Contrasena" in label else ""
            entry = tk.Entry(self, font=("Nunito", 13), bd=0, bg="#ffffff", fg="#1f2a44", show=show_char)
            self.entries[label] = entry
            self.canvas.create_window(187, y + 36, window=entry, width=319, height=42)

        crear_btn = tk.Button(
            self,
            text="Crear Cuenta",
            font=("Nunito", 14, "bold"),
            bg="#2ecc71",
            fg="#ffffff",
            activebackground="#2ecc71",
            activeforeground="#ffffff",
            bd=0,
            command=lambda: self.controller.show_screen("HomeScreen"),
        )
        self.canvas.create_window(187, 610, window=crear_btn, width=319, height=48)

        volver_btn = tk.Button(
            self,
            text="Volver a Login",
            font=("Nunito", 12, "bold"),
            bg="#ffffff",
            fg="#1565c0",
            activebackground="#ffffff",
            activeforeground="#1565c0",
            bd=1,
            command=lambda: self.controller.show_screen("LoginScreen"),
        )
        self.canvas.create_window(187, 672, window=volver_btn, width=319, height=44)
