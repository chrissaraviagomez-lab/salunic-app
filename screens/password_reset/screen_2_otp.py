import tkinter as tk
from tkinter import Canvas

class Screen2OTP(tk.Frame):
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
        self.create_otp_inputs()
        self.create_resend_text()
        self.create_info_box()
        self.create_buttons()
    
    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
    
    def create_blur_circles(self):
        circles = [(205, -70, 115, "#e91e8c"), (-55, 557, 92.5, "#2ecc71"),
                   (275, 341, 67.5, "#4fc3f7"), (-15, 373, 55, "#ffd600")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="")
    
    def create_status_bar(self):
        self.canvas.create_text(24, 30, text="9:41 AM", font=("Nunito", 12, "bold"),
                               fill="#ffffff", anchor="w")
        self.canvas.create_text(351, 30, text="100%", font=("Nunito", 12, "bold"),
                               fill="#ffffff", anchor="e")
    
    def create_header(self):
        self.canvas.create_oval(24, 43, 62, 81, fill="#ffffff", outline="")
        self.canvas.create_oval(26, 45, 60, 79, fill="#34c759", outline="")
        self.canvas.create_text(43, 62, text="S", font=("Arial", 20, "bold"), fill="#ffffff")
        self.canvas.create_text(85, 62, text="SALUNIC", font=("Nunito", 15, "bold"),
                               fill="#ffffff", anchor="w")
    
    def create_progress_bar(self):
        self.canvas.create_rectangle(22, 127, 127.66, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(134.66, 127, 240.33, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(247.33, 127, 353, 132, fill="#ffffff", outline="")
        self.canvas.create_rectangle(22, 152, 126.39, 176, fill="#4fc3f7", outline="", width=0)
        self.canvas.create_text(35, 164, text="PASO 2 DE 3", font=("Nunito", 10, "bold"),
                               fill="#4fc3f7", anchor="w")
    
    def create_title(self):
        self.canvas.create_text(22, 114, text="Revisa tu correo", font=("Nunito", 21, "bold"),
                               fill="#ffffff", anchor="nw")
    
    def create_description(self):
        self.canvas.create_text(22, 179, text="Ingresa el código de 6 dígitos enviado a maria@gmail.com",
                               font=("Nunito", 12.5), fill="#ffffff", anchor="nw", width=339)
    
    def create_otp_inputs(self):
        otp_positions = [(22, 212.55), (78.83, 212.55), (135.66, 212.55),
                        (192.52, 212.55), (249.33, 212.55), (306.17, 212.55)]
        colors = ["#2ecc71", "#2ecc71", "#4fc3f7",
                 "#ffffff", "#ffffff", "#ffffff"]
        numbers = ["5", "8", "", "", "", ""]
        
        for (x, y), color, num in zip(otp_positions, colors, numbers):
            self.canvas.create_rectangle(x, y, x + 46.84, y + 56, fill=color,
                                       outline="#ffffff" if "white" in color else "",
                                       width=1 if "white" in color else 0)
            if num:
                self.canvas.create_text(x + 23.42, y + 28, text=num, font=("Nunito", 22, "bold"),
                                       fill="#ffffff")
    
    def create_resend_text(self):
        self.canvas.create_text(187.5, 284.55, text="¿No recibiste el código? Reenviar 02:45",
                               font=("Nunito", 12), fill="#ffffff", justify="center")
    
    def create_info_box(self):
        self.canvas.create_rectangle(22, 310.55, 353, 393.19, fill="#ffd600", outline="", width=0)
        self.canvas.create_text(37, 325.55, text="El código expira en 5 minutos. Revisa también la carpeta de spam. Puedes solicitar un nuevo código.",
                               font=("Nunito", 11.5), fill="#ffffff", anchor="nw", width=194)
    
    def create_buttons(self):
        self.canvas.create_rectangle(22, 415.2, 353, 465.2, fill="#2ecc71", outline="", width=0)
        self.canvas.create_text(187.5, 440.2, text="VERIFICAR CÓDIGO", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
        self.canvas.create_rectangle(22, 473.2, 353, 520.2, fill="#ffffff", outline="", width=0)
        self.canvas.create_text(187.5, 496.5, text="CAMBIAR CORREO", font=("Nunito", 14, "bold"),
                               fill="#ffffff")
