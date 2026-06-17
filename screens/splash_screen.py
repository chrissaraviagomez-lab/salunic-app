import tkinter as tk
from tkinter import Canvas
from screens.inicio_screen import InicioScreen

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1565c0")
        self.controller = controller
        self.canvas = Canvas(self, width=375, height=812, bg="#1565c0", highlightthickness=0)
        self.canvas.pack()

        self.create_background()
        self.create_logo()
        self.create_title()
        self.create_tagline()
        self.create_loader()
        self.after(2500, lambda: controller.show_frame(InicioScreen))

    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#1565c0", outline="")
        circles = [(330, -40, 120, "#1976d2"), (-60, 700, 130, "#0d47a1")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                   fill=color, outline="")

    def create_logo(self):
        self.canvas.create_oval(137, 270, 237, 370, fill="#ffffff", outline="")
        self.canvas.create_oval(141, 274, 233, 366, fill="#2ecc71", outline="")
        self.canvas.create_text(187, 320, text="S", font=("Arial", 48, "bold"), fill="#ffffff")

    def create_title(self):
        self.canvas.create_text(187, 400, text="SALUNIC", font=("Nunito", 32, "bold"), fill="#ffffff")

    def create_tagline(self):
        self.canvas.create_text(187, 440, text="Salud y Bienestar Nicaragua",
                               font=("Nunito", 14), fill="rgba(255, 255, 255, 0.72)")

    def create_loader(self):
        self.canvas.create_rectangle(87, 720, 287, 726, fill="rgba(255, 255, 255, 0.2)", outline="")
        self.canvas.create_rectangle(87, 720, 187, 726, fill="#2ecc71", outline="")
        self.canvas.create_text(187, 750, text="Cargando...", font=("Nunito", 13),
                               fill="rgba(255, 255, 255, 0.6)")
