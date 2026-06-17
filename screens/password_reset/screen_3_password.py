import tkinter as tk
from tkinter import Canvas
from screens.inicio_screen import InicioScreen

class Screen3Password(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack()

        self.create_background()
        self.create_blur_circles()
        self.create_status_bar()
        self.create_header()
        self.create_progress_bar()
        self.create_title()
        self.create_description()
        self.create_password_fields()
        self.create_requirements()
        self.create_buttons()

    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")

    def create_blur_circles(self):
        circles = [(205, -70, 115, "#e91e8c"), (-55, 557, 92.5, "#2ecc71"),
                   (275, 341, 67.5, "#4fc3f7"), (-15, 373, 55, "#ffd600")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                                   fill=color, outline="")

    def create_status_bar(self):
        self.canvas.create_text(24, 30, text="9:41 AM", font=("Nunito", 12, "bold"),
                               fill="rgba(255, 255, 255, 0.82)", anchor="w")
        self.canvas.create_text(351, 30, text="100%", font=("Nunito", 12, "bold"),
                               fill="rgba(255, 255, 255, 0.82)", anchor="e")

    def create_header(self):
        self.canvas.create_oval(24, 43, 62, 81, fill="#ffffff", outline="")
        self.canvas.create_oval(26, 45, 60, 79, fill="#34c759", outline="")
        self.canvas.create_text(43, 62, text="S", font=("Arial", 20, "bold"), fill="#ffffff")
        self.canvas.create_text(85, 62, text="SALUNIC", font=("Nunito", 15, "bold"),
                               fill="#ffffff", anchor="w")

    def create_progress_bar(self):
        self.canvas.create_rectangle(22, 127, 127.66, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(134.66, 127, 240.33, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(247.33, 127, 353, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(22, 152, 126.39, 176,
                                    fill="rgba(46, 204, 113, 0.14)", outline="", width=0)
        self.canvas.create_text(35, 164, text="PASO 3 DE 3", font=("Nunito", 10, "bold"),
                               fill="#2ecc71", anchor="w")

    def create_title(self):
        self.canvas.create_text(22, 114, text="Nueva contraseña", font=("Nunito", 21, "bold"),
                               fill="#ffffff", anchor="nw")

    def create_description(self):
        self.canvas.create_text(22, 179,
                               text="Crea una contraseña segura para proteger tu cuenta SALUNIC",
                               font=("Nunito", 12.5), fill="rgba(255, 255, 255, 0.5)",
                               anchor="nw", width=339)

    def create_password_fields(self):
        # Nueva contraseña
        self.canvas.create_text(22, 230, text="NUEVA CONTRASEÑA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 253, 353, 287,
                                    fill="rgba(255, 255, 255, 0.13)", outline="")
        self.canvas.create_text(50, 270, text="••••••••••••", font=("Nunito", 18),
                               fill="rgba(255, 255, 255, 0.5)")

        # Fortaleza de contraseña
        strengths = [("#2ecc71", 22), ("#2ecc71", 92.5), ("#ffd600", 163), ("#e0e0e0", 233.5)]
        for color, x in strengths:
            self.canvas.create_rectangle(x, 298, x + 58.5, 303, fill=color, outline="")
        self.canvas.create_text(22, 313, text="Contraseña fuerte", font=("Nunito", 10.5),
                               fill="#2ecc71", anchor="nw")

        # Confirmar contraseña
        self.canvas.create_text(22, 340, text="CONFIRMAR CONTRASEÑA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 363, 353, 397,
                                    fill="rgba(255, 255, 255, 0.13)", outline="")
        self.canvas.create_text(50, 380, text="••••••••••••", font=("Nunito", 18),
                               fill="rgba(255, 255, 255, 0.5)")

    def create_requirements(self):
        self.canvas.create_text(22, 420, text="REQUISITOS DE LA CONTRASEÑA",
                               font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        requirements = [
            (True, "Mínimo 8 caracteres"),
            (True, "Al menos una letra mayúscula"),
            (True, "Al menos un número"),
            (False, "Al menos un carácter especial (!@#$%)"),
        ]
        for i, (met, text) in enumerate(requirements):
            y = 445 + i * 22
            color = "#2ecc71" if met else "rgba(255, 255, 255, 0.35)"
            icon = "✓" if met else "○"
            self.canvas.create_text(22, y, text=icon, font=("Arial", 12, "bold"),
                                   fill=color, anchor="w")
            self.canvas.create_text(42, y, text=text, font=("Nunito", 12),
                                   fill=color, anchor="w")

    def create_buttons(self):
        btn_save = self.canvas.create_rectangle(22, 570, 353, 620, fill="#2ecc71", outline="", width=0)
        self.canvas.create_text(187.5, 595, text="GUARDAR CONTRASEÑA", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
        self.canvas.tag_bind(btn_save, "<Button-1>",
                             lambda e: self.controller.show_frame(InicioScreen))

        self.canvas.create_rectangle(22, 630, 353, 677,
                                    fill="rgba(255, 255, 255, 0.07)", outline="", width=0)
        self.canvas.create_text(187.5, 653, text="CANCELAR", font=("Nunito", 14, "bold"),
                               fill="rgba(255, 255, 255, 0.82)")
