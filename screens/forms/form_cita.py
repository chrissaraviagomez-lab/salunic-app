import tkinter as tk
from tkinter import Canvas

class FormCita(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack()

        self.create_background()
        self.create_blur_circles()
        self.create_status_bar()
        self.create_header()
        self.create_title()
        self.create_form_fields()

    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")

    def create_blur_circles(self):
        circles = [(210, -65, 110, "#e91e8c"), (-50, 577, 87.5, "#2ecc71"),
                   (275, 341, 65, "#4fc3f7")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                   fill=color, outline="")

    def create_status_bar(self):
        self.canvas.create_text(22, 30, text="9:41", font=("Nunito", 12, "bold"),
                               fill="rgba(255, 255, 255, 0.82)")
        self.canvas.create_text(345, 30, text="100%", font=("Nunito", 12, "bold"),
                               fill="rgba(255, 255, 255, 0.82)")

    def create_header(self):
        self.canvas.create_oval(22, 43, 60, 81, fill="#ffffff", outline="")
        self.canvas.create_oval(24, 45, 58, 79, fill="#34c759", outline="")
        self.canvas.create_text(41, 62, text="S", font=("Arial", 18, "bold"), fill="#ffffff")
        self.canvas.create_text(72.5, 62, text="SALUNIC", font=("Nunito", 15, "bold"), fill="#ffffff")

    def create_title(self):
        self.canvas.create_text(22, 86, text="Reservar cita", font=("Nunito", 20, "bold"),
                               fill="#ffffff")
        self.canvas.create_text(22, 120, text="Agenda tu próxima consulta médica",
                               font=("Nunito", 12.5), fill="rgba(255, 255, 255, 0.48)")

    def create_form_fields(self):
        # Especialidad
        self.canvas.create_text(22, 160, text="ESPECIALIDAD *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 183, 353, 217, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 200, text="Medicina General", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.82)")

        # Doctor
        self.canvas.create_text(22, 242, text="MÉDICO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 265, 353, 299, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 282, text="Dr. Carlos Ruiz", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")

        # Fecha
        self.canvas.create_text(22, 324, text="FECHA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 347, 162.5, 381, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 364, text="15/06/2025", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")

        # Hora
        self.canvas.create_text(182.5, 324, text="HORA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(182.5, 347, 323, 381, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(205.5, 364, text="10:30 AM", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")

        # Motivo
        self.canvas.create_text(22, 406, text="MOTIVO DE CONSULTA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 429, 353, 510, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 446, text="Describe el motivo de tu consulta...",
                               font=("Nunito", 13), fill="rgba(255, 255, 255, 0.28)", anchor="nw",
                               width=290)

        # Tipo de atención
        self.canvas.create_text(22, 535, text="TIPO DE ATENCIÓN", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        types = [(22, "Presencial", True), (130, "Teleconsulta", False)]
        for x, label, active in types:
            color = "rgba(46, 204, 113, 0.18)" if active else "rgba(255, 255, 255, 0.07)"
            text_color = "#2ecc71" if active else "rgba(255, 255, 255, 0.55)"
            self.canvas.create_rectangle(x, 558, x + 96, 585, fill=color, outline="")
            self.canvas.create_text(x + 48, 571.5, text=label, font=("Nunito", 12),
                                   fill=text_color)

        # Notas adicionales
        self.canvas.create_text(22, 618, text="NOTAS ADICIONALES", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 641, 353, 692, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 658, text="Información adicional para el médico...",
                               font=("Nunito", 13), fill="rgba(255, 255, 255, 0.28)", anchor="nw",
                               width=290)

        # Botón
        self.canvas.create_rectangle(22, 720, 353, 770, fill="#2ecc71", outline="")
        self.canvas.create_text(187.5, 745, text="CONFIRMAR CITA", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
