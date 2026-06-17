import tkinter as tk
from tkinter import Canvas


class InicioScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f4f6fb")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#f4f6fb", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_ui()

    def _draw_ui(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#f4f6fb", outline="")
        self.canvas.create_rectangle(0, 0, 375, 266, fill="#1565c0", outline="")

        self.canvas.create_text(22, 74, text="Bienvenido a", font=("Nunito", 16, "bold"), fill="#dbeafe", anchor="nw")
        self.canvas.create_text(22, 101, text="SALUNIC", font=("Nunito", 37, "bold"), fill="#ffffff", anchor="nw")
        self.canvas.create_text(
            22,
            157,
            text="Tu plataforma de salud y bienestar con citas, medicamentos y seguimiento médico.",
            font=("Nunito", 12),
            fill="#c8e1ff",
            anchor="nw",
            width=330,
        )

        cards = [
            (22, 300, "📅", "Citas", "Agenda y recuerda tus consultas"),
            (22, 402, "💊", "Medicamentos", "Control de dosis y horarios"),
            (22, 504, "📋", "Historial", "Consulta tu evolución clínica"),
        ]
        for x, y, icon, title, subtitle in cards:
            self.canvas.create_rectangle(x, y, 353, y + 85, fill="#ffffff", outline="")
            self.canvas.create_text(x + 24, y + 29, text=icon, font=("Arial", 23), fill="#1565c0")
            self.canvas.create_text(x + 66, y + 22, text=title, font=("Nunito", 14, "bold"), fill="#1a1a2e", anchor="nw")
            self.canvas.create_text(x + 66, y + 47, text=subtitle, font=("Nunito", 11), fill="#6b7280", anchor="nw")

        self.canvas.create_rectangle(22, 645, 353, 695, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 670, text="COMENZAR", font=("Nunito", 15, "bold"), fill="#ffffff")

        self.canvas.create_rectangle(22, 705, 353, 753, fill="#ffffff", outline="#d5dce5")
        self.canvas.create_text(188, 729, text="INICIAR SESIÓN", font=("Nunito", 14, "bold"), fill="#1565c0")
