import tkinter as tk
from tkinter import Canvas


class Screen3Password(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_ui()

    def _draw_ui(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
        self.canvas.create_rectangle(0, 0, 375, 232, fill="#1565c0", outline="")

        self.canvas.create_text(22, 92, text="Nueva contraseña", font=("Nunito", 28, "bold"), fill="#ffffff", anchor="nw")
        self.canvas.create_text(
            22,
            138,
            text="Crea una contraseña segura para proteger tu cuenta.",
            font=("Nunito", 12),
            fill="#c8e1ff",
            anchor="nw",
            width=320,
        )

        fields = [
            (22, 286, "NUEVA CONTRASEÑA", "••••••••••"),
            (22, 366, "CONFIRMAR CONTRASEÑA", "••••••••••"),
        ]
        for x, y, label, value in fields:
            self.canvas.create_text(x, y, text=label, font=("Nunito", 10, "bold"), fill="#8f98ab", anchor="nw")
            self.canvas.create_rectangle(x, y + 22, 353, y + 62, fill="#f4f6fb", outline="#e7ebf2")
            self.canvas.create_text(x + 16, y + 42, text=value, font=("Nunito", 16, "bold"), fill="#1a1a2e", anchor="w")

        self.canvas.create_rectangle(22, 470, 353, 520, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 495, text="ACTUALIZAR CONTRASEÑA", font=("Nunito", 15, "bold"), fill="#ffffff")

        self.canvas.create_text(188, 560, text="Usa al menos 8 caracteres con letras y números.",
                                font=("Nunito", 11), fill="#8f98ab", justify="center")
