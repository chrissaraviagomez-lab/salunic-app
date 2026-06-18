import tkinter as tk
from tkinter import Canvas


class InicioScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f4f6fb")
        self.controller = controller

        self.canvas = Canvas(self, width=375, height=812, bg="#f4f6fb", highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 375, 812, fill="#f4f6fb", outline="")
        self.canvas.create_rectangle(0, 0, 375, 240, fill="#1565c0", outline="")
        self.canvas.create_text(28, 72, text="SALUNIC", font=("Nunito", 24, "bold"), fill="#ffffff", anchor="w")
        self.canvas.create_text(
            28,
            112,
            text="Tu aplicacion de salud para controlar citas, medicamentos y bienestar.",
            font=("Nunito", 12),
            fill="#ffffff",
            anchor="w",
            width=320,
        )

        self.canvas.create_text(28, 284, text="Caracteristicas principales", font=("Nunito", 16, "bold"), fill="#1565c0", anchor="w")

        cards = [
            (28, 318, "Citas medicas", "Gestion de consultas y agenda personal"),
            (28, 412, "Medicamentos", "Recordatorios y seguimiento diario"),
            (28, 506, "Panel de control", "Resumen rapido de tu estado de salud"),
        ]
        for x, y, title, subtitle in cards:
            self.canvas.create_rectangle(x, y, 347, y + 76, fill="#ffffff", outline="#dbe3f5")
            self.canvas.create_text(x + 16, y + 23, text=title, font=("Nunito", 13, "bold"), fill="#1565c0", anchor="w")
            self.canvas.create_text(x + 16, y + 50, text=subtitle, font=("Nunito", 11), fill="#5c6b8a", anchor="w")

        comenzar_btn = tk.Button(
            self,
            text="Comenzar",
            font=("Nunito", 14, "bold"),
            bg="#2ecc71",
            fg="#ffffff",
            activebackground="#2ecc71",
            activeforeground="#ffffff",
            bd=0,
            command=lambda: self.controller.show_screen("LoginScreen"),
        )
        self.canvas.create_window(187, 696, window=comenzar_btn, width=319, height=48)

        login_btn = tk.Button(
            self,
            text="Iniciar Sesion",
            font=("Nunito", 14, "bold"),
            bg="#ffffff",
            fg="#1565c0",
            activebackground="#ffffff",
            activeforeground="#1565c0",
            bd=1,
            command=lambda: self.controller.show_screen("LoginScreen"),
        )
        self.canvas.create_window(187, 758, window=login_btn, width=319, height=48)
