import tkinter as tk
from tkinter import Canvas

class FormMedicamento(tk.Frame):
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
    
    def create_title(self):
        self.canvas.create_text(22, 125, text="Agregar medicamento", font=("Nunito", 20, "bold"),
                               fill="#ffffff")
        self.canvas.create_text(22, 160, text="Registra un nuevo medicamento para tu tratamiento activo",
                               font=("Nunito", 12), fill="rgba(255, 255, 255, 0.48)")
    
    def create_form_fields(self):
        # Nombre del medicamento
        self.canvas.create_text(22, 200, text="NOMBRE DEL MEDICAMENTO *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 225, 353, 259, fill="rgba(255, 255, 255, 0.13)", outline="")
        self.canvas.create_text(50, 242, text="Ej: Metformina 500mg", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Dosis y Presentación
        self.canvas.create_text(22, 288, text="DOSIS *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 313, 162.5, 347, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 330, text="500mg", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        self.canvas.create_text(182.5, 288, text="PRESENTACIÓN", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(182.5, 313, 323, 347, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(187.5, 330, text="Tableta", font=("Nunito", 13),
                               fill="rgba(255, 255, 255, 0.82)")
        
        # Frecuencia
        self.canvas.create_text(22, 376, text="FRECUENCIA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        
        frequencies = [(22, "1X DÍA", False), (89.79, "2X DÍA", True), (157.55, "3X DÍA", False),
                      (225.79, "CADA 8H", False)]
        for x, freq, active in frequencies:
            color = "rgba(46, 204, 113, 0.18)" if active else "rgba(255, 255, 255, 0.07)"
            text_color = "#2ecc71" if active else "rgba(255, 255, 255, 0.55)"
            self.canvas.create_rectangle(x, 401, x + 57, 428, fill=color,
                                       outline="rgba(46, 204, 113, 0.5)" if active else "rgba(255, 255, 255, 0.14)")
            self.canvas.create_text(x + 28.5, 414, text=freq, font=("Nunito", 11),
                                   fill=text_color)
        
        # Horarios
        self.canvas.create_text(22, 457, text="HORARIOS DE TOMA *", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        
        self.canvas.create_rectangle(22, 480, 162.5, 514, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(45, 497, text="8:00 AM", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        self.canvas.create_rectangle(182.5, 480, 323, 514, fill="rgba(255, 255, 255, 0.13)", outline="")
        self.canvas.create_text(205.5, 497, text="1:00 PM", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Instrucciones
        self.canvas.create_text(22, 560, text="INSTRUCCIONES ESPECIALES", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 585, 353, 619, fill="rgba(255, 255, 255, 0.1)", outline="")
        self.canvas.create_text(50, 602, text="Ej: Tomar con alimentos", font=("Nunito", 13.5),
                               fill="rgba(255, 255, 255, 0.28)")
        
        # Imagen
        self.canvas.create_text(22, 640, text="IMAGEN DE LA RECETA", font=("Nunito", 10.5, "bold"),
                               fill="rgba(255, 255, 255, 0.5)")
        self.canvas.create_rectangle(22, 660, 353, 728, fill="rgba(255, 255, 255, 0.04)", outline="",
                                   width=0)
        self.canvas.create_text(187.5, 685, text="📸", font=("Arial", 26))
        self.canvas.create_text(187.5, 715, text="Toca para tomar foto o subir imagen de tu receta médica",
                               font=("Nunito", 11.5), fill="rgba(255, 255, 255, 0.42)",
                               justify="center", width=289)
        
        # Checkbox
        self.canvas.create_rectangle(22, 750, 42, 770, fill="#2ecc71", outline="")
        self.canvas.create_text(32, 760, text="✓", font=("Arial", 12, "bold"), fill="#ffffff")
        self.canvas.create_text(57, 750, text="Activar recordatorio con notificación push en los horarios indicados",
                               font=("Nunito", 12), fill="rgba(255, 255, 255, 0.62)", anchor="nw", width=262)
