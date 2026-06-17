import tkinter as tk
from tkinter import Canvas

class FormRegistro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.canvas = Canvas(self, width=375, height=812, bg="#ffffff", highlightthickness=0)
        self.canvas.pack()
        
        self.create_background()
        self.create_blur_circles()
        self.create_status_bar()
        self.create_header()
        self.create_progress()
        self.create_title()
        self.create_form_fields()
    
    def create_background(self):
        self.canvas.create_rectangle(0, 0, 375, 812, fill="#ffffff", outline="")
    
    def create_blur_circles(self):
        circles = [(210, -65, 110, "#e91e8c"), (-50, 577, 87.5, "#2ecc71"),
                   (275, 341, 65, "#4fc3f7")]
        for x, y, radius, color in circles:
            self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="")
    
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
    
    def create_progress(self):
        self.canvas.create_rectangle(22, 127, 147.09, 132, fill="#2ecc71", outline="")
        self.canvas.create_rectangle(154.09, 127, 279.18, 132, fill="rgba(255, 255, 255, 0.14)", outline="")
        self.canvas.create_rectangle(286.18, 127, 411, 132, fill="rgba(255, 255, 255, 0.14)", outline="")
    
    def create_title(self):
        self.canvas.create_text(22, 86, text="Crear cuenta", font=("Nunito", 20, "bold"),
                               fill="#ffffff")
        self.canvas.create_text(22, 120, text="Completa tu información personal para comenzar en Salunic",
                               font=("Nunito", 12.5), fill="rgba(255, 255, 255, 0.48)")
    
    def create_form_fields(self):
        # Foto de perfil
        self.canvas.create_oval(22, 175, 82, 235, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(52, 205, text="📷", font=("Arial", 22), fill="#ffffff")
        self.canvas.create_text(97, 190, text="Foto de perfil", font=("Nunito", 14, "bold"),
                               fill="#ffffff", anchor="nw")
        self.canvas.create_text(97, 210, text="Opcional: jpg o png", font=("Nunito", 11),
                               fill="rgba(255, 255, 255, 0.45)", anchor="nw")
        
        # Campos de nombre y apellido
        self.canvas.create_text(22, 262, text="NOMBRE *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 285, 162.5, 319, fill="rgba(255, 255, 255, 0.1)", outline="",
                                   width=0)
        self.canvas.create_text(45, 302, text="María", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        self.canvas.create_text(182.5, 262, text="APELLIDO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(182.5, 285, 323, 319, fill="rgba(255, 255, 255, 0.1)", outline="",
                                   width=0)
        self.canvas.create_text(205.5, 302, text="González", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Email
        self.canvas.create_text(22, 334, text="CORREO ELECTRÓNICO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 357, 353, 391, fill="rgba(255, 255, 255, 0.13)", outline="",
                                   width=0)
        self.canvas.create_text(50, 374, text="tucorreo@email.com", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Teléfono
        self.canvas.create_text(22, 416, text="TELÉFONO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 439, 353, 473, fill="rgba(255, 255, 255, 0.1)", outline="",
                                   width=0)
        self.canvas.create_text(50, 456, text="505-8888-0000", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Checksum
        self.canvas.create_rectangle(22, 553, 42, 573, fill="#2ecc71", outline="")
        self.canvas.create_text(32, 563, text="✓", font=("Arial", 12, "bold"), fill="#ffffff")
        self.canvas.create_text(57, 560, text="Acepto los términos y condiciones y la política de privacidad de Salunic",
                               font=("Nunito", 12), fill="rgba(255, 255, 255, 0.6)", anchor="nw", width=278)
        
        # Botón
        self.canvas.create_rectangle(22, 620, 353, 670, fill="#2ecc71", outline="")
        self.canvas.create_text(187.5, 645, text="CREAR MI CUENTA", font=("Nunito", 15, "bold"),
                               fill="#ffffff")
