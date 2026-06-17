import tkinter as tk
from tkinter import Canvas


class Screen1Email(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_ui()

    def _draw_ui(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
        self.canvas.create_rectangle(0, 0, 375, 232, fill="#1565c0", outline="")

        self.canvas.create_text(22, 92, text="Recuperar contraseña", font=("Nunito", 26, "bold"), fill="#ffffff", anchor="nw")
        self.canvas.create_text(
            22,
            136,
            text="Ingresa tu correo para enviarte un código de verificación.",
            font=("Nunito", 12),
            fill="#c8e1ff",
            anchor="nw",
            width=320,
        )

        self.canvas.create_text(22, 286, text="CORREO ELECTRÓNICO", font=("Nunito", 10, "bold"), fill="#8f98ab", anchor="nw")
        self.canvas.create_rectangle(22, 308, 353, 348, fill="#f4f6fb", outline="#e7ebf2")
        self.canvas.create_text(40, 328, text="maria@gmail.com", font=("Nunito", 13), fill="#1a1a2e", anchor="w")

        self.canvas.create_rectangle(22, 380, 353, 430, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 405, text="ENVIAR CÓDIGO", font=("Nunito", 15, "bold"), fill="#ffffff")
    
        self.canvas.create_text(
            188,
            470,
            text="Te llegará un código de 6 dígitos válido por 5 minutos.",
            font=("Nunito", 11),
            fill="#8f98ab",
            width=300,
            justify="center",
        )
