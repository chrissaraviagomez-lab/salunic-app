import tkinter as tk
from tkinter import Canvas


class FormCita(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_ui()

    def _draw_ui(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
        self.canvas.create_rectangle(0, 0, 375, 210, fill="#1565c0", outline="")

        self.canvas.create_text(22, 78, text="Reservar cita", font=("Nunito", 28, "bold"), fill="#ffffff", anchor="nw")
        self.canvas.create_text(
            22,
            126,
            text="Selecciona especialidad, fecha y horario para programar tu consulta médica.",
            font=("Nunito", 12),
            fill="#c8e1ff",
            anchor="nw",
            width=328,
        )

        fields = [
            (22, 250, "ESPECIALIDAD", "Medicina General"),
            (22, 330, "DOCTOR", "Dra. Ana López"),
            (22, 410, "FECHA", "22 Jun 2026"),
            (22, 490, "HORA", "10:30 AM"),
            (22, 570, "MOTIVO", "Control mensual"),
        ]
        for x, y, label, value in fields:
            self.canvas.create_text(x, y, text=label, font=("Nunito", 10, "bold"), fill="#8f98ab", anchor="nw")
            self.canvas.create_rectangle(x, y + 22, 353, y + 58, fill="#f4f6fb", outline="#e7ebf2")
            self.canvas.create_text(x + 14, y + 40, text=value, font=("Nunito", 13), fill="#1a1a2e", anchor="w")

        self.canvas.create_rectangle(22, 680, 353, 730, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 705, text="CONFIRMAR CITA", font=("Nunito", 15, "bold"), fill="#ffffff")
