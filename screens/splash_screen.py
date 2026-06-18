import tkinter as tk
from tkinter import Canvas


class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f4f6fb")
        self.controller = controller
        self.progress = 0
        self.animation_id = None
        self.navigate_id = None

        self.canvas = Canvas(self, width=375, height=812, bg="#f4f6fb", highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 375, 812, fill="#f4f6fb", outline="")
        self.canvas.create_oval(125, 250, 250, 375, fill="#1565c0", outline="")
        self.canvas.create_text(187, 312, text="S", font=("Nunito", 40, "bold"), fill="#ffffff")
        self.canvas.create_text(187, 420, text="SALUNIC", font=("Nunito", 28, "bold"), fill="#1565c0")
        self.canvas.create_text(187, 456, text="Salud y Bienestar", font=("Nunito", 14), fill="#2ecc71")
        self.canvas.create_text(187, 550, text="Bienvenido", font=("Nunito", 16, "bold"), fill="#1565c0")

        self.canvas.create_rectangle(38, 585, 337, 603, fill="#dbe3f5", outline="")
        self.progress_bar = self.canvas.create_rectangle(38, 585, 38, 603, fill="#2ecc71", outline="")

    def on_show(self):
        if self.animation_id:
            self.after_cancel(self.animation_id)
        if self.navigate_id:
            self.after_cancel(self.navigate_id)

        self.progress = 0
        self.canvas.coords(self.progress_bar, 38, 585, 38, 603)
        self.animate_progress()
        self.navigate_id = self.after(3000, lambda: self.controller.show_screen("InicioScreen"))

    def animate_progress(self):
        self.progress = min(self.progress + 1, 100)
        progress_width = 38 + int(299 * self.progress / 100)
        self.canvas.coords(self.progress_bar, 38, 585, progress_width, 603)
        if self.progress < 100:
            self.animation_id = self.after(30, self.animate_progress)
