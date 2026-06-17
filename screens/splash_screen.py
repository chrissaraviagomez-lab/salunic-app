import tkinter as tk
from tkinter import Canvas


class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#0f4c81")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#0f4c81", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self._draw_ui()

    def _draw_ui(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#0f4c81", outline="")
        self.canvas.create_oval(110, 250, 265, 405, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 328, text="S", font=("Nunito", 70, "bold"), fill="#ffffff")
        self.canvas.create_text(188, 455, text="SALUNIC", font=("Nunito", 34, "bold"), fill="#ffffff")
        self.canvas.create_text(
            188,
            495,
            text="Salud y Bienestar Nicaragua",
            font=("Nunito", 13, "bold"),
            fill="#d2e7f8",
        )

        self.canvas.create_rectangle(55, 625, 320, 635, fill="#0a365a", outline="")
        self.canvas.create_rectangle(55, 625, 205, 635, fill="#2ecc71", outline="")
        self.canvas.create_text(188, 664, text="Cargando...", font=("Nunito", 12, "bold"), fill="#d2e7f8")
