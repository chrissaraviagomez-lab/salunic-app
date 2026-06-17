import tkinter as tk
from tkinter import Canvas
from screens.password_reset.screen_2_otp import Screen2OTP

class Screen1Email(tk.Frame):
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
        self.create_email_field()
        self.create_info_box()
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
        self.canvas.create_rectangle(134.66, 127, 240.33, 132,
                                    fill="rgba(255, 255, 255, 0.14)", outline="")
        self.canvas.create_rectangle(247.33, 127, 353, 132,
                                    fill="rgba(255, 255, 255, 0.14)", outline="")
        self.canvas.create_rectangle(22, 152, 126.39, 176,
                                    fill="rgba(79, 195, 247, 0.14)", outline="", width=0)
        self.canvas.create_text(35, 164, text="PASO 1 DE 3", font=("Nunito", 10, "bold"),
                               fill="#4fc3f7", anchor="w")

    def create_title(self):
        self.canvas.create_text(22, 114, text="Recupera tu cuenta", font=("Nunito", 21, "bold"),
                               fill="#ffffff", anchor="nw")

    def create_description(self):
        self.canvas.create_text(22, 179,
                               text="Ingresa el correo electrónico asociado a tu cuenta SALUNIC",
                               font=("Nunito", 12.5), fill="rgba(255, 255, 255, 0.5)",
                               anchor="nw", width=339)

    def create_email_field(self):
        self.canvas.create_text(22, 230, text="CORREO ELECTRÓNICO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 253, 353, 287,
                                    fill="rgba(255, 255, 255, 0.13)", outline="")
        self.canvas.create_text(50, 270, text="tucorreo@email.com", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")

    def create_info_box(self):
        self.canvas.create_rectangle(22, 310, 353, 390,
                                    fill="rgba(79, 195, 247, 0.07)", outline="", width=0)
        self.canvas.create_text(37, 325,
                               text="Te enviaremos un código de verificación a tu correo. "
                                    "Asegúrate de revisar también la carpeta de spam.",
                               font=("Nunito", 11.5), fill="rgba(255, 255, 255, 0.6)",
                               anchor="nw", width=300)

    def create_buttons(self):
        btn_send = self.canvas.create_rectangle(22, 415, 353, 465, fill="#2ecc71", outline="", width=0)
        self.canvas.create_text(187.5, 440, text="ENVIAR CÓDIGO", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
        self.canvas.tag_bind(btn_send, "<Button-1>",
                             lambda e: self.controller.show_frame(Screen2OTP))

        self.canvas.create_rectangle(22, 473, 353, 520,
                                    fill="rgba(255, 255, 255, 0.07)", outline="", width=0)
        self.canvas.create_text(187.5, 496.5, text="VOLVER AL INICIO", font=("Nunito", 14, "bold"),
                               fill="rgba(255, 255, 255, 0.82)")
