import tkinter as tk
from tkinter import Canvas
from screens.home_screen import HomeScreen
from screens.forms.form_registro import FormRegistro

class InicioScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack()

        self.create_background()
        self.create_header()
        self.create_welcome_text()
        self.create_features()
        self.create_buttons()

    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
        self.canvas.create_rectangle(0, 0, 375, 320, fill="#1565c0", outline="")
        circles = [(330, -30, 110, "#1976d2"), (-50, 260, 90, "#0d47a1")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                   fill=color, outline="")

    def create_header(self):
        self.canvas.create_oval(22, 43, 62, 83, fill="#ffffff", outline="")
        self.canvas.create_oval(24, 45, 60, 81, fill="#2ecc71", outline="")
        self.canvas.create_text(41, 64, text="S", font=("Arial", 20, "bold"), fill="#ffffff")
        self.canvas.create_text(75, 64, text="SALUNIC", font=("Nunito", 16, "bold"),
                               fill="#ffffff", anchor="w")

    def create_welcome_text(self):
        self.canvas.create_text(187, 170, text="Bienvenido a SALUNIC",
                               font=("Nunito", 22, "bold"), fill="#ffffff")
        self.canvas.create_text(187, 210, text="Tu plataforma de salud y bienestar en Nicaragua",
                               font=("Nunito", 13), fill="rgba(255, 255, 255, 0.72)",
                               justify="center", width=300)

    def create_features(self):
        features = [
            (375 // 2, 390, "📅", "Gestión de Citas", "Agenda y monitorea tus citas médicas"),
            (375 // 2, 490, "💊", "Control de Medicamentos", "Recordatorios y seguimiento de medicación"),
            (375 // 2, 590, "📋", "Historial Médico", "Accede a tu historial clínico completo"),
        ]
        for x, y, icon, title, desc in features:
            self.canvas.create_oval(x - 30, y - 25, x + 30, y + 25, fill="#e8f5e9", outline="")
            self.canvas.create_text(x, y, text=icon, font=("Arial", 24))
            self.canvas.create_text(x, y + 45, text=title, font=("Nunito", 14, "bold"), fill="#1a1a2e")
            self.canvas.create_text(x, y + 65, text=desc, font=("Nunito", 11),
                                   fill="#9aa0b2", justify="center", width=280)

    def create_buttons(self):
        btn_login = self.canvas.create_rectangle(22, 690, 353, 740, fill="#1565c0", outline="")
        self.canvas.create_text(187, 715, text="INICIAR SESIÓN", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
        self.canvas.tag_bind(btn_login, "<Button-1>",
                             lambda e: self.controller.show_frame(HomeScreen))

        btn_register = self.canvas.create_rectangle(22, 752, 353, 799, fill="#2ecc71", outline="")
        self.canvas.create_text(187, 776, text="CREAR CUENTA", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
        self.canvas.tag_bind(btn_register, "<Button-1>",
                             lambda e: self.controller.show_frame(FormRegistro))
